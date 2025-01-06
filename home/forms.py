from django import forms

class SubscriberForm(forms.Form):
    email = forms.EmailField(label='Your email', max_length=100)
