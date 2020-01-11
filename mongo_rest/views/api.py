import os
from django.core.management.base import BaseCommand
from django.http import HttpResponse
from django.views import View
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
import json
load_dotenv()


class SpotAPIView(View):
    def get(self, request):

        # connect to "mongo_rest_db" via internal network
        client = MongoClient("mongodb://mongo_rest_db:27017/")

        # authenticate to mongodb
        db = client[os.getenv("MONGODB_DATABASE")]
        db.authenticate(os.getenv("MONGODB_USERNAME"),
                        os.getenv("MONGODB_PASSWORD"))

        # get/create empty collections
        buildings = db.buildings
        spots = db.spots

        # example queries - ids are excluded from the final results
        # query = spots.find({})
        # query = spots.find({"_id": ObjectId("5e0e2d2ec852de2cd7e0cfe4")}, {"_id": 0})
        # query = spots.find({"building.code": "KNE"}, {"_id": 0})

   
        query = spots.aggregate([
            {"$match": {}},
            {"$lookup":
                {
                    "from": "buildings",
                    "localField": "building_id",
                    "foreignField": "_id",
                    "as": "blah"
                }
            },
        ])

        # bson.json_util "dumps" - used for converting bson data to json
        results = query

        return HttpResponse(results)
