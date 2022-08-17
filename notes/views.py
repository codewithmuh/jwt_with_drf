
# notes/views.py
from rest_framework import viewsets
from .models import Notes
from serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    notes = Notes.objects.all()
    serializer_class = NoteSerializer