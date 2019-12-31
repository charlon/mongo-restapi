import os
from django.core.management.base import BaseCommand
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.dbref import DBRef
load_dotenv()


class Command(BaseCommand):
    def handle(self, **options):

        # connect to 'mongo_rest_db' via internal network
        client = MongoClient("mongodb://mongo_rest_db:27017/")

        # provide creds
        db = client[os.getenv("MONGODB_DATABASE")]
        db.authenticate(os.getenv("MONGODB_USERNAME"),
                        os.getenv("MONGODB_PASSWORD"))

        print(db.name)

        # list the collections
        collections = db.list_collection_names()
        print(collections)

        # get/create empty collection
        buildings = db["buildings"]
        spots = db["spots"]

        # check if collections have data... drop them and start fresh
        if ("spots" or "buildings") in collections:
            print("dropping data")
            if (buildings.count()):
                buildings.drop()
            if (spots.count()):
                spots.drop()

        # buildings json
        buildingList = [
            {
                "name": "Mary Gates Hall",
                "code": "MGH",
                "hours": "asdfjadsf"
            },
            {
                "name": "Odegaard Undergraduate Library",
                "code": "OUG",
                "hours": "asdfjadsf"
            },
            {
                "name": "Johnson Hall",
                "code": "JHN",
                "hours": "asdfjadsf"
            },
            {
                "name": "Kane Hall",
                "code": "KNE",
                "hours": "asdfjadsf"
            },
            {
                "name": "Suzzallo Library",
                "code": "SUZ",
                "hours": "asdfjadsf"
            }
        ]

        buildings.insert_many(buildingList)

        # spots json
        spotList = [
            {
                "name": "Mary Gates Espresso",
                "type": "cafe",
                "building": buildings.find_one({"name": "Mary Gates Hall"})
            },
            {
                "name": "Motosurf",
                "type": "food truck",
                "building": buildings.find_one({"name": "Odegaard Undergraduate Library"})
            },
            {
                "name": "Sunrise Griddle",
                "type": "food truck",
                "building": buildings.find_one({"name": "Johnson Hall"})
            },
            {
                "name": "DUB Street Burgers, Husky Den",
                "type": "food court",
                "building": buildings.find_one({"name": "Kane Hall"})
            },
            {
                "name": "Pagliacci Pizza, Husky Den",
                "type": "food court",
                "building": buildings.find_one({"name": "Suzzallo Library"})
            }
        ]

        spots.insert_many(spotList)
