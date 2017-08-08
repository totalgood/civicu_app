from rest_framework import serializers
from labeler.models import Image


class ImageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    caption = serializers.CharField("Description of the image, where and when it was taken",
                                    max_length=512, default=None, null=True)
    uploaded_by = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Image.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.caption = validated_data.get('caption', instance.caption)
        instance.save()
        return instance
