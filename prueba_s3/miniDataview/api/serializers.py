from rest_framework import serializers
from miniDataview.models import Log, Station, Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ["name"]
class StationSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(read_only=True)
    class Meta:
        model = Station
        fields = ["name", "organization"]


class LogSerializer(serializers.ModelSerializer):
    station = StationSerializer(read_only=True)

    class Meta:
        model = Log
        fields = ["name", "station"]