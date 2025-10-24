from rest_framework import viewsets, permissions
from miniDataview.models import Log
from miniDataview.api.serializers import LogSerializer

class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    permission_classes = [permissions.IsAuthenticated]