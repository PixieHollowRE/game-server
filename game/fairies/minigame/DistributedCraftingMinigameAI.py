from game.fairies.instance.DistributedInstanceBaseAI import DistributedInstanceBaseAI

class DistributedCraftingMinigameAI(DistributedInstanceBaseAI):
    def __init__(self, air) -> None:
        super().__init__(air)

        self.professionId: int = 0

    def setProfessionID(self, professionId):
        # CRAFT_TYPE_TAILORING = 0
        # CRAFT_TYPE_BAKING = 1
        # CRAFT_TYPE_TINKERING = 2
        self.professionId = professionId

    def setCommunityDyeIDList():
        # Array of dye IDs
        pass

    def setRecipeChoice():
        # Current Recipe ID, 1 or 2
        # CRAFT_STYLE_COMMUNITY = 1
        # CRAFT_STYLE_PERSONAL = 2
        pass

    def setResults():
        # setResults(
        #   this.currentRecipeID,
        #   _loc1_ (quality score?),
        #   int(this._resultValues[MMOConstants.TAILORING_PRIMARY_COLOR]),
        #   int(this._resultValues[MMOConstants.TAILORING_SECONDARY_COLOR]),
        #   this.qualityList.length
        # )
        pass

    def setEmbellishResults():
        # Seems to be empty function in Client
        pass

    def craftingResponse():
        # If param1 !=1 throws an App Panic with invalidCraftError
        pass
