from rest_framework import serializers
from .models import Image
from .validators import ImageValidator


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.CharField(validators=[ImageValidator()])

    class Meta:
        model = Image
        fields = ('id', 'description', 'image', 'created_at')