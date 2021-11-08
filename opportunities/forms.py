from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, ModelForm
from .models import Job, Skills


# creating a form
class AddJobForm(ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Job

        # specify fields to be used
        fields = [
            "author",
            "title",
            "company",
            "employment_type",
            "salary",
            "description",
            "application_status",
        ]

        widgets = {
            'author': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Job Title'
                }),
            'company': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'employment_type': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'salary': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'description': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'application_status': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                })                                                                                                  
        }


class AddSkillForm(forms.ModelForm):
    class Meta:
        model = Skills

        fields = ["name"]