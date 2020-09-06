from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'description', 'deadline')


class MarkAsCompletedForm(forms.Form):
    completed = forms.BooleanField()
