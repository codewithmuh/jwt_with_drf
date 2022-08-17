
from rest_framework import serializers
from .models import Notes


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "title", "content", "created", "updated")
        model = Notes
