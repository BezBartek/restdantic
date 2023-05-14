from rest_framework import serializers


class SampleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
