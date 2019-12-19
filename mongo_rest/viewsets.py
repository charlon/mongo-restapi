from rest_framework_mongoengine import viewsets
from mongo_rest.serializers import SpotSerializer
from mongo_rest.models import Spot


class SpotViewSet(viewsets.ModelViewSet):
    '''
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    '''
    lookup_field = 'id'
    serializer_class = SpotSerializer

    def get_queryset(self):
        return Spot.objects.all()
