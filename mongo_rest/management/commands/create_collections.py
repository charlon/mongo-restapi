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
        collist = db.list_collection_names()

        # check if collections exist, else create empty collections
        if ("spots" or "buildings") in collist:
            print(collist)
        else:

            #create collections
            buildingCollection = db["buildings"]
            spotCollection = db["spots"]

            # seed buildings
            buildingList = [
                {"name": "Mary Gates Hall (MGH)"},
                {"name": "Odegaard Undergraduate Library (OUG)"},
                {"name": "Johnson Hall (JHN)"},
                {"name": "Kane Hall (KNE)"},
                {"name": "Suzzallo Library (SUZ)"}
            ]

            buildingCollection.insert_many(buildingList)

            # seed spots
            spotList = [
                {
                    "name": "Mary Gates Espresso",
                    "type": "cafe",
                    "building": "blah"
                },
                {
                    "name": "Motosurf",
                    "type": "food truck",
                    "building": "blah"
                },
                {
                    "name": "Sunrise Griddle",
                    "type": "food truck",
                    "building : "blah"
                },
                {
                    "name": "DUB Street Burgers, Husky Den",
                    "type": "food court",
                    "building": "blah"
                },
                {
                    "name": "Pagliacci Pizza, Husky Den",
                    "type": "food court",
                    "building": "blah"
                }
            ]

            spotCollection.insert_many(spotList)
