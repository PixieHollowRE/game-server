from paths import XML
from game.fairies.badges import badge_events
from game.fairies.instance.DistributedInstanceBaseAI import DistributedInstanceBaseAI
from game.fairies.minigame.recipe import recipe_parser
from game.fairies.ai.BakingAssets import BAKED_ITEMS
from game.fairies.ai.FairiesConstants import get_item_type

DEFAULT_XML = XML / "recipes.xml"

MIN_QUALITY = 0
MAX_QUALITY = 100

class DistributedCraftingMinigameAI(DistributedInstanceBaseAI):
    def __init__(self, air) -> None:
        super().__init__(air)

        self.professionId = 0
        self.recipeChoice: dict[int, tuple[int, int]] = {} # avId -> (recipeId, craftingStyle)

    def setProfessionID(self, professionId: int):
        # CRAFT_TYPE_TAILORING = 0
        # CRAFT_TYPE_BAKING = 1
        # CRAFT_TYPE_TINKERING = 2
        self.professionId = professionId

    def getProfessionID(self) -> int:
        return self.professionId

    def setCommunityDyeIDList(self):
        # Array of dye IDs
        pass

    def getCommunityDyeIDList(self) -> list:
        return [45, 50, 53, 54, 38]

    def setRecipeChoice(self, recId, style):
        # Current Recipe ID, 1 or 2
        # CRAFT_STYLE_COMMUNITY = 2
        # CRAFT_STYLE_PERSONAL = 1
        avId = self.air.getAvatarIdFromSender()
        self.recipeChoice[avId] = (recId, style)

    def setResults(self, recipeId, quality, color1, color2, length):
        avId = self.air.getAvatarIdFromSender()

        choice = self.recipeChoice.get(avId)
        if choice is None:
            print(f"setResults called by avId={avId} with no prior setRecipeChoice - we should ignore this.")
            return
        
        recId, craftingStyle = choice

        if craftingStyle == 2:
            # CRAFT_STYLE_COMMUNITY: practice. Nothing is made and nothing is
            # spent, but a practice craft is exactly what the practice ladder
            # counts, so bank it before bailing out of the item-granting path.
            eventId = badge_events.PROFESSION_TO_PRACTICE_EVENT.get(self.professionId)

            if eventId is not None:
                self.air.badgeManager.d_accumulate(avId, eventId)

            self.recipeChoice.pop(avId, None)
            return
        
        avatar = self.air.doId2do.get(avId)
        if avatar is None:
            print(f"setResults: no avatar object for avId={avId}")
            self.recipeChoice.pop(avId, None)
            return

        recipes = recipe_parser.parse_recipes(DEFAULT_XML, recId)
        if not recipes:
            print("something broke - fix it or else you dummy dumbo dimwit")
            self.recipeChoice.pop(avId, None)
            return

        recipe = recipes[0]

        quality = max(MIN_QUALITY, min(MAX_QUALITY, quality))

        if not self._removeRecipeIngredients(avId, avatar, recipe):
            print(f"setResults: avId={avId} missing ingredients for recId={recId}, aborting")
            self.recipeChoice.pop(avId, None)
            return
        
        if not self._removeDyes(avId, avatar, color1, color2):
            print(f"setResults: avId={avId} missing dyes for recId={recId}, aborting")
            self.recipeChoice.pop(avId, None)
            return  

        if recId in BAKED_ITEMS:
            self._giveBakedItem(avId, avatar, recId, quality)
        else:
            self._giveCraftedItem(avId, avatar, recId, quality, color1, color2)

        self.air.mongoInterface.recordStat(avId, "recipe", recId, quality)

        # One event per item produced. Community-style crafts bailed out above
        # (they advance the practice ladder instead); reaching here means a
        # personal craft that spent ingredients and made something, so it counts
        # toward the personal ladder.
        eventId = badge_events.PROFESSION_TO_PERSONAL_EVENT.get(self.professionId)

        if eventId is not None:
            self.air.badgeManager.d_accumulate(avId, eventId)

        self.recipeChoice.pop(avId, None)

    def _removeRecipeIngredients(self, avId, avatar, recipe):
        for ingredient in recipe.ingredients:
            removed = self.air.inventoryManager.removeIngredientsFromPouch(
                avId, ingredient.item_id, ingredient.amount
            )
            if not removed:
                return False
        avatar.d_syncPouchAfterChanges()
        return True

    def _removeDyes(self, avId, avatar, color1, color2):
        removed_any = False
        for color in (color1, color2):
            if color:
                dye_id = color + 14000
                removed = self.air.inventoryManager.removeIngredientsFromPouch(avId, dye_id, 1)
                if not removed:
                    return False
                removed_any = True
        if removed_any:
            avatar.d_syncPouchAfterChanges()
        return True

    def _giveBakedItem(self, avId, avatar, itemId, quality):
        if 96 <= quality <= 100:
            amount = 6
        elif 81 <= quality <= 95:
            amount = 3
        else:
            amount = 2

        if self.air.inventoryManager.addIngredientsToPouch(avId, itemId, amount, -1):
            print("adding:", itemId, amount)
            avatar.d_setPouch(self.air.inventoryManager.getPouch(avId))

    def _giveCraftedItem(self, avId, avatar, recipeId, quality, color1, color2):

        if get_item_type(recipeId) in ("Furniture", "Lamp", "Decoration"):
            self._grant_home(avId, avatar, recipeId, quality, color1, color2)
        else:
            self._grant_wardrobe(avId, avatar, recipeId, quality, color1, color2)

    def _grant_item(self, avId, avatar, recipeId, quality, color1, color2, location, update_name) -> bool:
        inv_id = self.air.mongoInterface.getNextDoId()
        itemType = get_item_type(recipeId)
        how_acquired = 11

        inv_item_ext = [
            inv_id,
            recipeId,
            -1,
            avId,
            avatar.getName(),
            0,
            "",
            quality,
            color1,
            color2,
            how_acquired,
        ]

        result = self.air.mongoInterface.mongodb.fairies.update_one(
            {"_id": avId},
            {
                "$push": {
                    "avatar.items": {
                        "inv_id": inv_id,
                        "type": itemType,
                        "item_id": recipeId,
                        "slot": -1,
                        "createdById": avId,
                        "createdByName": avatar.getName(),
                        "giftedById": 0,
                        "giftedByName": "",
                        "quality": quality,
                        "color1": color1,
                        "color2": color2,
                        "howAcquired": how_acquired,
                        "location": location,
                    }
                }
            },
        )

        if result.modified_count == 0:
            return False

        self.air.inventoryManager.sendUpdateToAvatarId(
            avId, update_name, [recipeId, inv_item_ext]
        )
        return True

    def _grant_wardrobe(self, avId, avatar, recipeId, quality, color1, color2) -> bool:
        return self._grant_item(avId, avatar, recipeId, quality, color1, color2, "Wardrobe", "wardrobeItem")

    def _grant_home(self, avId, avatar, recipeId, quality, color1, color2) -> bool:
        return self._grant_item(avId, avatar, recipeId, quality, color1, color2, "Storage", "storageItem")

    def setEmbellishResults(self):
        # Seems to be empty function in Client
        pass

    def craftingResponse(self):
        # If param1 !=1 throws an App Panic with invalidCraftError
        pass
