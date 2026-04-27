from game.fairies.instance.DistributedInstanceBaseAI import DistributedInstanceBaseAI

class DistributedCraftingMinigameAI(DistributedInstanceBaseAI):
    def __init__(self, air) -> None:
        super().__init__(air)

        self.professionId: int = 1

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

    def setRecipeChoice(self):
        # Current Recipe ID, 1 or 2
        # CRAFT_STYLE_COMMUNITY = 1
        # CRAFT_STYLE_PERSONAL = 2
        pass

    def setResults(self):
        # setResults(
        #   this.currentRecipeID,
        #   _loc1_ (quality score),
        #   int(this._resultValues[MMOConstants.TAILORING_PRIMARY_COLOR]),
        #   int(this._resultValues[MMOConstants.TAILORING_SECONDARY_COLOR]),
        #   this.qualityList.length
        # )
        pass

    def setEmbellishResults(self):
        # Seems to be empty function in Client
        pass

    def craftingResponse(self):
        # If param1 !=1 throws an App Panic with invalidCraftError
        pass
