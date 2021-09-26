from django.conf import settings
from rest_framework import viewsets, mixins
# from .serializers import CameraRegistrySerializer, CameraRetrieveSerializer, StreamRegistrySerializer
from .models import Example


class ExampleRegistry(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """Представление для модели Example"""

    def get_queryset(self):
        pass
        # return models.Camera.objects.all().filter(is_visible=True)

    def get_serializer_class(self):
        # return CameraRegistrySerializer
        pass

    def get_serializer_class_for_retrieve(self):
        # return CameraRetrieveSerializer
        pass

    def retrieve(self, request, *args, **kwargs):
        # instance = self.get_object()
        # serializer = self.get_serializer_class_for_retrieve()(instance, context={"request": request})
        # return Response(serializer.data)
        pass
