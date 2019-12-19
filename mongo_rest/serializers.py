from rest_framework_mongoengine import serializers
from mongo_rest.models import Spot


class SpotSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Spot
        fields = '__all__'
