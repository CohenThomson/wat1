from django import forms
from .models import Flashcard, Subject

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name'] 

class CardForm(forms.ModelForm):
    class Meta:
        model = Flashcard  # Change from Card to Flashcard
        fields = ['question', 'answer', 'image']  # Include the 'image' field if needed

        #add images maybe