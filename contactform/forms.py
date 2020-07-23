from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=20,required = True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class ReplyForm(forms.Form):
    pid = forms.CharField(required=True)
    reply_message = forms.CharField(widget = forms.Textarea, max_length = 150,required = True)

class Deletequery(forms.Form):
    TRUE_FALSE_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )

    deletequery = forms.ChoiceField(choices = TRUE_FALSE_CHOICES, label="Select",initial='', widget=forms.Select())