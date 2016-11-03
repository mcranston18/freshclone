from rest_framework.viewsets import ModelViewSet

from clients.models import Client
from clients.serializers import ClientSerializer


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()