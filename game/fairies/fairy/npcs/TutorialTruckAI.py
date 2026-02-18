from game.fairies.carplayer.InteractiveObjectAI import (
    CMD_TYPE_POSITIVE, COMMAND_OFFER_QUERY_INTERACTIONS,
    COMMAND_SET_MAP_EFFECT, TYPE_NPC, InteractiveObjectAI)


class TutorialTruckAI(InteractiveObjectAI):
    def __init__(self, air) -> None:
        # HACK: Renaming our class name here because
        # DistributedObjectAI will search dclassesByName
        # for the non-existant TutorialTruckAI dclass.
        self.__class__.__name__ = "InteractiveObjectAI"

        InteractiveObjectAI.__init__(self, air)

        self.objType = TYPE_NPC
        self.assetId = 31024 # truckCatalogItemId
        self.clientScript = "scripts/interactive/truck.lua"
        self.name = "Truck"

    def announceGenerate(self) -> None:
        InteractiveObjectAI.announceGenerate(self)

        # Experiments
        # TODO: More accurate position
        self.d_setTelemetry(1019, 521, 0, 1640, -860, 4362, 5259, 41770)
