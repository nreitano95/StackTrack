from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, ModelForm
from .models import Job, Skills, Contacts


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
            "skills"
        ]
        # widgets
        widgets = {"author": forms.HiddenInput()}
    skills = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Skills.objects.all().order_by('name'),
        widget=forms.CheckboxSelectMultiple
    )


class AddSkillForm(forms.ModelForm):
    class Meta:
        model = Skills

        fields = ["name"]


class AddContactForm(forms.ModelForm):
    class Meta:
        model = Contacts

        fields = [
            "user",
            "first_name",
            "last_name",
            "company_name",
            "email",
        ]

        widgets = {"user": forms.HiddenInput()}
