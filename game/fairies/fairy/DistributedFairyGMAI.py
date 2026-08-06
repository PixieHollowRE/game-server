from .DistributedFairyPlayerAI import DistributedFairyPlayerAI

class DistributedFairyGMAI(DistributedFairyPlayerAI):
    def __init__(self, air) -> None:
        DistributedFairyPlayerAI.__init__(self, air)

    def ignoresRealmCapacity(self) -> bool:
        # Staff go where they need to. The client already exempts
        # DistributedFairyGM from the shard chooser's full-realm greyout and
        # from the home population lock; this matches that server-side.
        return True
