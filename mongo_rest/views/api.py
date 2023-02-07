# Copyright 2022 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

import os
from django.core.management.base import BaseCommand
from django.http import HttpResponse
from django.views import View
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps


class SpotAPIView(View):
    def get(self, request):

        # connect to "mongo_rest_db" via internal network
        client = MongoClient(
            os.getenv("MONGODB_CLIENT"),
            username=os.getenv("MONGODB_ROOT_USERNAME"),
            password=os.getenv("MONGODB_ROOT_PASSWORD"),
        )

        # get database
        db = client[os.getenv("MONGODB_DATABASE")]

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

        query = spots.aggregate(
            [
                {"$match": {}},
                {
                    "$lookup": {
                        "from": "buildings",
                        "foreignField": "_id",
                        "localField": "building_id",
                        "as": "building",
                    }
                },
            ]
        )

        # bson.json_util "dumps" - used for converting bson data to json
        results = dumps(query)

        return HttpResponse(results)
