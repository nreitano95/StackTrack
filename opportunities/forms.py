from django import forms
from django.contrib.auth.models import User
<<<<<<< HEAD
from django.forms import TextInput, ModelForm
from .models import Job, Skills
=======
from .models import Job, Skills, Contacts
>>>>>>> master


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
                'placeholder': 'Company'
                }),
            'employment_type': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Employment Type'
                }),
            'salary': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Salary'
                }),
            'description': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Description'
                }),
            'application_status': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Enter the Status'
                })                                                                                                  
        }


class AddSkillForm(forms.ModelForm):
    class Meta:
        model = Skills

<<<<<<< HEAD
        fields = ["name"]
=======
        fields = ["name"]


class AddContactForm(forms.ModelForm):
    class Meta:
        model = Contacts

        fields = [
            "user",
            "firstname",
            "lastname",
            "companyname",
            "email",
        ]
>>>>>>> master
