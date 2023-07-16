from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
