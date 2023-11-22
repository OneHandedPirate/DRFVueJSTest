from rest_framework import serializers


class ImageValidator:
    def __call__(self, value):
        if not value.startswith("data:image"):
            raise serializers.ValidationError("Некорректный формат файла")
