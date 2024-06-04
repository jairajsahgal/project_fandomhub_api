"""Serializers for Reviews App."""

from rest_framework import serializers

from .models import Review


class ReviewReadSerializer(serializers.ModelSerializer):
    """Serializer for Review model (List/retrieve)."""

    user = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = [
            "id",
            "user",
            "rating",
            "comment",
            "is_spoiler",
            "created_at",
            "updated_at",
        ]


class ReviewWriteSerializer(serializers.ModelSerializer):
    """Serializer for Review model (Create/update)."""

    class Meta:
        model = Review
        fields = [
            "comment",
            "is_spoiler",
            "rating",
        ]
