from .models import Example
from rest_framework import serializers


class ExampleSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Example"""

    class Meta:
        model = Example
        fields = ('id', 'name', 'title', 'content', 'is_active', 'image')
