import os
from django.core.management.base import BaseCommand
from dotenv import load_dotenv
from pymongo import MongoClient
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

        # check if collections exist, else create empty collections
        if ("spots" or "buildings") in collections:
            print(collections)
        else:

            # create collections

            buildings = db["buildings"]
            spots = db["spots"]

            # seed buildings
            buildingList = [
                {"name": "Mary Gates Hall", "code": "MGH"},
                {"name": "Odegaard Undergraduate Library", "code": "OUG"},
                {"name": "Johnson Hall", "code": "JHN"},
                {"name": "Kane Hall", "code": "KNE"},
                {"name": "Suzzallo Library", "code": "SUZ"}
            ]

            buildings.insert_many(buildingList)

            # seed spots
            spotList = [
                {
                    "name": "Mary Gates Espresso",
                    "type": "cafe"
                },
                {
                    "name": "Motosurf",
                    "type": "food truck"
                },
                {
                    "name": "Sunrise Griddle",
                    "type": "food truck"
                },
                {
                    "name": "DUB Street Burgers, Husky Den",
                    "type": "food court"
                },
                {
                    "name": "Pagliacci Pizza, Husky Den",
                    "type": "food court"
                }
            ]

            spots.insert_many(spotList)
