import os
from django.core.management.base import BaseCommand
from django.http import HttpResponse
from django.views import View
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.dbref import DBRef
from bson.json_util import dumps
load_dotenv()


class SpotAPIView(View):
    def get(self, request):

        # connect to 'mongo_rest_db' via internal network
        client = MongoClient("mongodb://mongo_rest_db:27017/")

        # authenticate to mongodb
        db = client[os.getenv("MONGODB_DATABASE")]
        db.authenticate(os.getenv("MONGODB_USERNAME"),
                        os.getenv("MONGODB_PASSWORD"))

        # get/create empty collections
        buildings = db["buildings"]
        spots = db["spots"]

        # API endpoint example: find all spots located in Kane Hall
        # dumps the query results into json format
        # kaneSpots = dumps(spots.find({"building.code": "KNE"}))
        # print(kaneSpots)

        # API endpoint example: find all spots
        # dumps the query results into json format
        allSpots = dumps(spots.find({}, {"_id": 0}))
        return HttpResponse(allSpots)
