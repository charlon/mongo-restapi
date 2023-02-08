import os
import json
from django.conf import settings
from django.core.management.base import BaseCommand
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.dbref import DBRef
from bson.json_util import dumps


class Command(BaseCommand):
    def handle(self, **options):

        # connect to 'mongo_rest_db' via internal network
        client = MongoClient(
            os.getenv("MONGODB_CLIENT"),
            username=os.getenv("MONGODB_ROOT_USERNAME"),
            password=os.getenv("MONGODB_ROOT_PASSWORD"),
        )

        # get database
        db = client[os.getenv("MONGODB_DATABASE")]

        # get/create empty collections
        buildings = db["buildings"]
        spots = db["spots"]
        airbnb = db["oahuListings"]

        # list the collections
        collections = db.list_collection_names()

        # check if collections have data... drop them and start fresh
        if ("spots" or "buildings") in collections:
            print("dropping collections")
            if buildings.count():
                buildings.drop()
            if spots.count():
                spots.drop()

        # buildings json
        buildingList = [
            {
                "name": "Mary Gates Hall",
                "code": "MGH",
                "hours": {
                    "monday": [["08:00", "21:00"]],
                    "tuesday": [["08:00", "21:00"]],
                    "wednesday": [["08:00", "21:00"]],
                    "thursday": [["08:00", "21:00"]],
                    "friday": [["08:00", "15:00"]],
                    "saturday": [["09:00", "17:00"]],
                    "sunday": [],
                },
            },
            {
                "name": "Odegaard Undergraduate Library",
                "code": "OUG",
                "hours": {
                    "monday": [["08:00", "21:00"]],
                    "tuesday": [["08:00", "21:00"]],
                    "wednesday": [["08:00", "21:00"]],
                    "thursday": [["08:00", "21:00"]],
                    "friday": [["08:00", "15:00"]],
                    "saturday": [["09:00", "17:00"]],
                    "sunday": [],
                },
            },
            {
                "name": "Johnson Hall",
                "code": "JHN",
                "hours": {
                    "monday": [["08:00", "21:00"]],
                    "tuesday": [["08:00", "21:00"]],
                    "wednesday": [["08:00", "21:00"]],
                    "thursday": [["08:00", "21:00"]],
                    "friday": [["08:00", "15:00"]],
                    "saturday": [["09:00", "17:00"]],
                    "sunday": [],
                },
            },
            {
                "name": "Kane Hall",
                "code": "KNE",
                "hours": {
                    "monday": [["08:00", "21:00"]],
                    "tuesday": [["08:00", "21:00"]],
                    "wednesday": [["08:00", "21:00"]],
                    "thursday": [["08:00", "21:00"]],
                    "friday": [["08:00", "15:00"]],
                    "saturday": [["09:00", "17:00"]],
                    "sunday": [],
                },
            },
            {
                "name": "Suzzallo Library",
                "code": "SUZ",
                "hours": {
                    "monday": [["08:00", "21:00"]],
                    "tuesday": [["08:00", "21:00"]],
                    "wednesday": [["08:00", "21:00"]],
                    "thursday": [["08:00", "21:00"]],
                    "friday": [["08:00", "15:00"]],
                    "saturday": [["09:00", "17:00"]],
                    "sunday": [],
                },
            },
        ]

        print("inserting buildings")
        buildings.insert_many(buildingList)

        # spots json
        # note.. including {"_id": 0} in the find query will exclude ids

        spotList = [
            {
                "name": "Mary Gates Espresso",
                "type": "cafe",
                "hours": {
                    "monday": [["08:00", "17:00"]],
                    "tuesday": [["08:00", "17:00"]],
                    "wednesday": [["08:00", "17:00"]],
                    "thursday": [["08:00", "17:00"]],
                    "friday": [["08:00", "13:00"]],
                    "saturday": [["09:00", "13:00"]],
                    "sunday": [],
                },
                "building_id": buildings.find_one({"code": "MGH"}).get("_id"),
            },
            {
                "name": "Motosurf",
                "type": "food truck",
                "hours": {
                    "monday": [["08:00", "17:00"]],
                    "tuesday": [["08:00", "17:00"]],
                    "wednesday": [["08:00", "17:00"]],
                    "thursday": [["08:00", "17:00"]],
                    "friday": [["08:00", "13:00"]],
                    "saturday": [["09:00", "13:00"]],
                    "sunday": [],
                },
                "building_id": buildings.find_one({"code": "OUG"}).get("_id"),
            },
            {
                "name": "Sunrise Griddle",
                "type": "food truck",
                "hours": {
                    "monday": [["08:00", "17:00"]],
                    "tuesday": [["08:00", "17:00"]],
                    "wednesday": [["08:00", "17:00"]],
                    "thursday": [["08:00", "17:00"]],
                    "friday": [["08:00", "13:00"]],
                    "saturday": [["09:00", "13:00"]],
                    "sunday": [],
                },
                "building_id": buildings.find_one({"code": "JHN"}).get("_id"),
            },
            {
                "name": "DUB Street Burgers, Husky Den",
                "type": "food court",
                "hours": {
                    "monday": [["08:00", "17:00"]],
                    "tuesday": [["08:00", "17:00"]],
                    "wednesday": [["08:00", "17:00"]],
                    "thursday": [["08:00", "17:00"]],
                    "friday": [["08:00", "13:00"]],
                    "saturday": [["09:00", "13:00"]],
                    "sunday": [],
                },
                "building_id": buildings.find_one({"code": "KNE"}).get("_id"),
            },
            {
                "name": "Pagliacci Pizza, Husky Den",
                "type": "food court",
                "hours": {
                    "monday": [["08:00", "17:00"]],
                    "tuesday": [["08:00", "17:00"]],
                    "wednesday": [["08:00", "17:00"]],
                    "thursday": [["08:00", "17:00"]],
                    "friday": [["08:00", "13:00"]],
                    "saturday": [["09:00", "13:00"]],
                    "sunday": [],
                },
                "building_id": buildings.find_one({"code": "SUZ"}).get("_id"),
            },
            {
                "name": "Pagliacci Pizza, Kane Basement",
                "type": "food court",
                "hours": {
                    "monday": [["08:00", "17:00"]],
                    "tuesday": [["08:00", "17:00"]],
                    "wednesday": [["08:00", "17:00"]],
                    "thursday": [["08:00", "17:00"]],
                    "friday": [["08:00", "13:00"]],
                    "saturday": [["09:00", "13:00"]],
                    "sunday": [],
                },
                "building_id": buildings.find_one({"code": "KNE"}).get("_id"),
            },
        ]

        print("inserting spots")
        spots.insert_many(spotList)

        # load airbnb data
        # https://bobbyhadz.com/blog/python-jsondecodeerror-extra-data
        with open(
            os.path.join(
                settings.BASE_DIR,
                "mongo_rest",
                "data",
                "updatedOahuListings.json",
            ),
            "r",
            encoding="utf-8",
        ) as f:
            file_data = json.load(f)

        airbnb.insert_many(file_data)

        client.close()
