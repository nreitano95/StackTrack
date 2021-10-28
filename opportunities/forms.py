from django import forms
from django.contrib.auth.models import User
from .models import Job, Skills


# creating a form
class AddJobForm(forms.ModelForm):

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


class AddSkillForm(forms.ModelForm):
    class Meta:
        model = Skills

        fields = ["name"]
