from pymongo import MongoClient, ReturnDocument

class MongoInterface:
    def __init__(self, air):
        self.air = air

        client = MongoClient(config.GetString("mongodb-host"))
        self.mongodb = client[config.GetString("mongodb-name")]

    def retrieveDocs(self, dclass: str, doId: int, queryField: str = "ownerDoId") -> list:
        cursor = getattr(self.mongodb, dclass)
        return list(cursor.find({queryField: doId})) or []

    def updateField(self, dclass: str, fieldName: str, doId: int, value, queryField: str = "_id"):
        queryData = {queryField: doId}
        updatedVal = {"$set": {fieldName: value}}

        table = getattr(self.mongodb, dclass)
        table.update_one(queryData, updatedVal)

    def updateFields(self, dclass: str, fields: dict, doId: int, queryField: str = "_id"):
        queryData = {queryField: doId}
        table = getattr(self.mongodb, dclass)

        updatedVal = {"$set": fields}
        table.update_one(queryData, updatedVal)

    def getNextDoId(self) -> int:
        table = self.mongodb.globals
        ret = table.find_one_and_update(
            {"_id": "doid"},
            {"$inc": {"seq": 1}},
            return_document=ReturnDocument.AFTER
        )
        return ret["seq"]
