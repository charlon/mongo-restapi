from rest_framework_mongoengine import serializers


class SpotSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Spot
        fields = '__all__'
