from rest_framework import serializers
from .models import Lines

class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lines
        fields = ['id', 'name', 'total']