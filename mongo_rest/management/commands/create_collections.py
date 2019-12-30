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
            db.create_collection('spots')
            db.create_collection('buildings')
