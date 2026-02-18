from game.fairies.carplayer.InteractiveObjectAI import (
    TYPE_NPC, InteractiveObjectAI)


class MaterAI(InteractiveObjectAI):
    def __init__(self, air) -> None:
        # HACK: Renaming our class name here because
        # DistributedObjectAI will search dclassesByName
        # for the non-existant MaterAI dclass.
        self.__class__.__name__ = "InteractiveObjectAI"

        InteractiveObjectAI.__init__(self, air)

        self.objType = TYPE_NPC
        self.assetId = 31009 # materCatalogItemId

    def announceGenerate(self) -> None:
        InteractiveObjectAI.announceGenerate(self)

        # Experiments
        self.d_setTelemetry(3329, 1889, 0, 13073, 6027, 12847, -32722, 325026)
