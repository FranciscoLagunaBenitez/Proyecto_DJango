"""
Definition of forms.
"""

from django import forms
from app.models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('name', 'publisher', 'year', 'genre', 'platform', 'score', 'online', 'pegi')

