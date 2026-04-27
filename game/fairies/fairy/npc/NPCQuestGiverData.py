from dataclasses import dataclass, field
from game.fairies.fairy.structs.FairyDNA import FairyDNA

@dataclass
class Questgiver:
    name: str
    questGiverId: int
    famousFairyId: int
    fairyDNA: FairyDNA = field(default_factory=FairyDNA)
    gender: int = 1

    def __post_init__(self):
        self.fairyDNA.gender = self.gender

    def to_tuple(self) -> tuple:
        return (self.name, self.fairyDNA.asTuple(), self.position, self.famousFairyID)

@dataclass
class QuestZone():
    zone: int
    questgiver: Questgiver

    def generate_quest_zone(self, DFQ_NPCAI):
        qzone = DFQ_NPCAI
        qzone.setName(self.questgiver.name)
        qzone.setFairyDNA(self.questgiver.fairyDNA.asTuple())
        qzone.setFamousFairyId(self.questgiver.famousFairyId)
        qzone.setQuestGiverId(self.questgiver.questGiverId)
        qzone.setRoomID(1)
        qzone.generateWithRequired(self.zone)
