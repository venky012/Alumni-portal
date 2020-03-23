from django import forms

class PostJobForm(forms.Form):
    last_date = forms.DateField(required = True,widget=forms.DateInput(format='%d/%m/%Y',
                            attrs={'placeholder': 'dd/mm/yyyy'}),input_formats=['%d/%m/%Y',])
    job_title = forms.CharField(max_length=50,required=True)
    category=forms.CharField(max_length=50,required=True)
    company = forms.CharField(max_length=50,required = True)
    place = forms.CharField(max_length= 50,required = True)
    experience = forms.CharField(max_length = 50,required = True)
    salary = forms.CharField(max_length = 20)

