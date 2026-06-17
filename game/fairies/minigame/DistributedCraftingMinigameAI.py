import os
from game.fairies.instance.DistributedInstanceBaseAI import DistributedInstanceBaseAI
from game.fairies.minigame.recipe import recipe_parser
from game.fairies.ai.BakingAssets import BAKED_ITEMS
from game.fairies.ai.FairiesConstants import get_item_type
from game.fairies.badges.StarterBadgeRegistry import (
    CRAFT_STYLE_PERSONAL,
    CRAFT_STYLE_PRACTICE,
)

DEFAULT_XML = os.path.join(os.path.dirname(__file__), "recipe/recipes.xml")

class DistributedCraftingMinigameAI(DistributedInstanceBaseAI):
    def __init__(self, air) -> None:
        super().__init__(air)

        self.professionId = 0 # This never seems to get set
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
        # recId = current recipe; style is CRAFT_STYLE_PERSONAL (1) or CRAFT_STYLE_PRACTICE (2).
        avId = self.air.getAvatarIdFromSender()
        self.recipeChoice[avId] = (recId, style)

    def setResults(self, recipeId, quality, color1, color2, length):
        avId = self.air.getAvatarIdFromSender()
        recId, craftingStyle = self.recipeChoice.get(avId, (recipeId, CRAFT_STYLE_PERSONAL))
        avatar = self.air.doId2do.get(avId)

        if craftingStyle == CRAFT_STYLE_PRACTICE:
            badge_manager = getattr(self.air, "badgeManager", None)
            if badge_manager is not None:
                badge_manager.applyCraftHelper(
                    avId, self.professionId, recipeId, craftingStyle
                )
            self.recipeChoice.pop(avId, None)
            return

        if avatar is None:
            self.notify.warning(f"setResults: no avatar on AI for avId={avId}")
            self.recipeChoice.pop(avId, None)
            return

        recipes = recipe_parser.parse_recipes(DEFAULT_XML, recipeId)
        if not recipes:
            self.notify.warning(f"setResults: recipe not found for recipeId={recipeId}")
            self.recipeChoice.pop(avId, None)
            return

        recipe = recipes[0]

        if not self._hasRecipeIngredients(avId, recipe):
            self.notify.warning(
                f"setResults: insufficient ingredients for recipeId={recipeId} avId={avId}"
            )
            self.recipeChoice.pop(avId, None)
            return

        if not self._hasDyes(avId, recipe, color1, color2):
            self.notify.warning(
                f"setResults: insufficient dyes for recipeId={recipeId} avId={avId}"
            )
            self.recipeChoice.pop(avId, None)
            return

        crafted = False
        if recipeId in BAKED_ITEMS:
            crafted = self._giveBakedItem(avId, avatar, recipeId, quality)
        else:
            crafted = self._giveCraftedItem(avId, avatar, recipeId, quality, color1, color2)

        if crafted:
            if not self._removeRecipeIngredients(avId, avatar, recipe):
                self.notify.warning(
                    f"setResults: grant succeeded but ingredient removal failed "
                    f"for recipeId={recipeId} avId={avId}"
                )
            elif not self._removeDyes(avId, avatar, recipe, color1, color2):
                self.notify.warning(
                    f"setResults: grant succeeded but dye removal failed "
                    f"for recipeId={recipeId} avId={avId}"
                )
            else:
                badge_manager = getattr(self.air, "badgeManager", None)
                if badge_manager is not None:
                    badge_manager.applyCraftHelper(
                        avId, self.professionId, recipeId, craftingStyle
                    )

        self.recipeChoice.pop(avId, None)

    def _hasRecipeIngredients(self, avId, recipe) -> bool:
        for ingredient in recipe.ingredients:
            if not self.air.inventoryManager.hasIngredientsInPouch(
                avId, ingredient.item_id, ingredient.amount
            ):
                return False
        return True

    def _hasDyes(self, avId, recipe, color1, color2) -> bool:
        if recipe.dye_count <= 0:
            return True
        for color in (color1, color2):
            if color:
                dye_id = color + 14000
                if not self.air.inventoryManager.hasIngredientsInPouch(avId, dye_id, 1):
                    return False
        return True

    def _removeRecipeIngredients(self, avId, avatar, recipe) -> bool:
        for ingredient in recipe.ingredients:
            if not self.air.inventoryManager.removeIngredientsFromPouch(
                avId, ingredient.item_id, ingredient.amount
            ):
                return False
        avatar.d_syncPouchAfterChanges()
        return True

    def _removeDyes(self, avId, avatar, recipe, color1, color2) -> bool:
        if recipe.dye_count <= 0:
            return True
        removed_any = False
        for color in (color1, color2):
            if color:
                dye_id = color + 14000
                if not self.air.inventoryManager.removeIngredientsFromPouch(avId, dye_id, 1):
                    return False
                removed_any = True
        if removed_any:
            avatar.d_syncPouchAfterChanges()
        return True

    def _giveBakedItem(self, avId, avatar, itemId, quality) -> bool:
        if 96 <= quality <= 100:
            amount = 6
        elif 81 <= quality <= 95:
            amount = 3
        else:
            amount = 2

        if self.air.inventoryManager.addIngredientsToPouch(avId, itemId, amount, -1):
            print("adding:", itemId, amount)
            avatar.d_setPouch(self.air.inventoryManager.getPouch(avId))
            return True
        return False

    def _giveCraftedItem(self, avId, avatar, recipeId, quality, color1, color2) -> bool:

        if get_item_type(recipeId) in ("Furniture", "Lamp", "Decoration"):
            return self._grant_home(avId, avatar, recipeId, quality, color1, color2)
        return self._grant_wardrobe(avId, avatar, recipeId, quality, color1, color2)


    def _grant_wardrobe(self, avId, avatar, recipeId, quality, color1, color2) -> bool:
        inv_id = self.air.mongoInterface.getNextDoId()
        itemType = get_item_type(recipeId)
        how_acquired = 11

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
                        "location": "Wardrobe",
                    }
                }
            },
        )

        if result.modified_count == 0:
            return False

        self.air.inventoryManager.sendUpdateToAvatarId(
            avId,
            "wardrobeItem",
            [
                recipeId,
                [
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
                ],
            ],
        )
        return True


    def _grant_home(self, avId, avatar, recipeId, quality, color1, color2) -> bool:
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
                        "location": "Storage",
                    }
                }
            },
        )

        if result.modified_count == 0:
            return False

        self.air.inventoryManager.sendUpdateToAvatarId(
            avId, "storageItem", [recipeId, inv_item_ext]
        )
        return True

    def setEmbellishResults(self):
        # Seems to be empty function in Client
        pass

    def craftingResponse(self):
        # If param1 !=1 throws an App Panic with invalidCraftError
        pass
