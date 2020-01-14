import os
from django.core.management.base import BaseCommand
from django.http import HttpResponse
from django.views import View
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
load_dotenv()


class SpotAPIView(View):
    def get(self, request):

        # connect to "mongo_rest_db" via internal network
        client = MongoClient("mongodb://mongo_rest_db:27017/")

        # authenticate to mongodb
        db = client[os.getenv("MONGODB_DATABASE")]
        db.authenticate(os.getenv("MONGODB_USERNAME"),
                        os.getenv("MONGODB_PASSWORD"))

        # get collections
        buildings = db.buildings
        spots = db.spots

        # example match queries
        # {"$match": {}}
        # {"$match": {"building_id": ObjectId("5e1e0f4445a0c1211b513aa1")}}
        # {"$match": {"type": "cafe"}}

        # $match all spots against the given "building_id", perform a $lookup
        # against the "buildings" collection...
        # the results are aggregated into a subdocument called "building"

        query = spots.aggregate([
            {"$match": {}},
            {"$lookup":
                {
                    "from": "buildings",
                    "foreignField": "_id",
                    "localField": "building_id",
                    "as": "building"
                }},
        ])

        # bson.json_util "dumps" - used for converting bson data to json
        results = dumps(query)

        return HttpResponse(results)
