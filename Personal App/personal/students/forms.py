from django import forms
from django.forms import ModelForm
from .models import studs
class roll_s(forms.Form):
    roll=forms.IntegerField(label="Your Roll No: ")
class indexes(forms.Form):
    Choices = [
    ('see_all', 'see all Students in the Database'),
    ('search', 'Search Specific students'),
    ('ent_info', 'Enter Information for students to be registered'),
    ('update','Update already exisitng database'),
    ]

    choice=forms.ChoiceField(choices=Choices,widget=forms.RadioSelect)
class ent_infos(ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'style':'width:10%'}),max_length=400)
    class Meta():
        model=studs
        fields='__all__'