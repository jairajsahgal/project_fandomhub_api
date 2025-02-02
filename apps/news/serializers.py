"""Serializers for News App."""

from rest_framework import serializers

from .models import New


class NewListSerializer(serializers.ModelSerializer):
    """Serializer for New model (List).."""

    tag = serializers.CharField(source="get_tag_display")
    author = serializers.SerializerMethodField()

    class Meta:
        model = New
        fields = [
            "id",
            "author",
            "title",
            "description",
            "image",
            "tag",
        ]
        read_only_fields = ["author"]

    def get_author(self, obj) -> str:
        return obj.author.username


class NewSerializer(serializers.ModelSerializer):
    """Serializer for New model."""

    tag = serializers.CharField(source="get_tag_display")

    class Meta:
        model = New
        fields = [
            "id",
            "author",
            "title",
            "description",
            "content",
            "image",
            "source",
            "tag",
            "created_at",
            "updated_at",
        ]
