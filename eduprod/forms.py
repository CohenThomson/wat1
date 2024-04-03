from django import forms


class CardCheckForm(forms.Form):
    card_id = forms.IntegerField(required=True)
    solved = forms.BooleanField(required=False)

#this form allows users to input a flashcard ID and mark whether it has been solved or not.