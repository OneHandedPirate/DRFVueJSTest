from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Image
from .serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    http_method_names = ('get', 'post', 'head', 'delete', 'options')
    queryset = Image.objects.all()
    permission_classes = [AllowAny]
