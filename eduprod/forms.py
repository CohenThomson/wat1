from django import forms

class CardForm(forms.Form):
    question = forms.CharField(label='question', max_length=255, default='')
    answer = forms.CharField(label='answer', max_length=255, default='')
    image = forms.ImageField(label='image', upload_to='flashcard_images', blank=True, null=True)
    subject = forms.CharField(label='subject', max_length=255, default='')   