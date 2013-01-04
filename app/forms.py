from django import forms
from models import *

class StudForm(forms.Form):
    first_name = forms.CharField(max_length=20,label="Name",widget=forms.TextInput(attrs={"placeholder":"Enter student name"}))
    second_name = forms.CharField(max_length=35,label="Surname",widget=forms.TextInput(attrs={"placeholder":"Enter student surname"}))
    patronymic = forms.CharField(max_length=25,widget=forms.TextInput(attrs={"placeholder":"Enter student patronymic"}))
    date_of_birth = forms.DateField(input_formats=["%d.%m.%Y","%d/%m/%Y","%d-%m-%Y"],widget=forms.TextInput(attrs={"placeholder":"Enter student birthday"}))
    group = forms.ModelChoiceField(queryset=Group.objects.all(),empty_label="Choose group",required=False,widget=forms.Select)

class GroupForm(forms.Form):
    name = forms.CharField(max_length=15,label="Name",widget=forms.TextInput(attrs={"placeholder":"Enter group name"}))
    warden = forms.ModelChoiceField(queryset=Student.objects.all(),empty_label="Choose warden",required=False,widget=forms.Select)

