from django import forms
from accounts.models import User

class ImageUploadForm(forms.Form):
    avatar = forms.ImageField()

class UpdateProfileForm(forms.Form):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    phone_number = forms.CharField(required=False)
    linkedin_url = forms.CharField(required=False)
    github_url = forms.CharField(required=False)
    webpage_url = forms.CharField(required=False)
    company = forms.CharField(required=False)
    summary = forms.CharField(required=False)
    place = forms.CharField(required=False)

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=50,required=True)
    email = forms.EmailField(max_length=200)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    phone_number = forms.CharField()
    linkedin_url = forms.CharField()
    github_url = forms.CharField()
    webpage_url = forms.CharField()
    passout_year = forms.CharField()
    company = forms.CharField()
    summary = forms.CharField()
    place = forms.CharField()
    conditions = forms.BooleanField()

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'phone_number',
                  'linkedin_url', 'github_url', 'webpage_url', 'passout_year', 'company', 'place', 'conditions','summary')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email,that is already taken')
        return email
