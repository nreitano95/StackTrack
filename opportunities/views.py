from typing import OrderedDict
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator

# from .models import <name of model class here>
from .models import Job, Skills, Contacts
from .forms import AddJobForm, AddSkillForm, AddContactForm
import requests
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def home(request):
    """Renders the Home page if not logged in and user's dashboard if logged in"""
    if request.user.is_authenticated:
        jobs = Job.objects.filter(author=request.user).all().order_by("company")
        context = {
            "jobs": jobs,
            "skills": Skills.objects.all(),
            "pending_apps": jobs.filter(application_status="Not Yet Applied"),
            "submitted_apps": jobs.filter(application_status="Applied"),
        }

        # Create Job Modal
        form = AddJobForm(request.POST or None, initial={"author": request.user})
        if form.is_valid():
            messages.success(request, "Job Created")
            form.save()
            return redirect("opportunities-home")

        context["form"] = form

        # Pie Chart of User's Skills
        # Create list of the foreign keys for the user's job's skills
        user_skills_fks = jobs.values_list('skills', flat=True)
        
        # Create a list of the values of the names of the user's job's skills
        user_skills = []
        
        try: 
            for skill_fk in user_skills_fks:
                skill = Skills.objects.get(id=skill_fk)
                user_skills.append(skill.name)
        except:
            pass

        # Generate data for the pie chart
        # Get the count of each skill from the my_
        data = []
        seen = []
        for skill in user_skills:
            if skill not in seen:
                data.append(user_skills.count(skill))
                seen.append(skill)

        # Generate labels for pie chart
        labels = []
        labels = list(OrderedDict.fromkeys(user_skills))

        # Set context fields for pie chart
        context["data"] = data
        context["labels"] = labels
        
        return render(request, "opportunities/dashboard.j2", context)
    return render(request, "opportunities/home.j2")


def about(request):
    """Renders the About page"""
    return render(request, "opportunities/about.j2", {"title": "About"})


@login_required
def jobs(request):
    """Renders the Jobs page"""
    context = {
        "jobs": Job.objects.filter(author=request.user).all().order_by("company")
    }

    # Create Job Modal
    form = AddJobForm(request.POST or None, initial={"author": request.user})
    if form.is_valid():
        messages.success(request, "Job Created")
        form.save()
        return redirect("opportunities-jobs")

    context["form"] = form

    return render(request, "opportunities/jobs.j2", context)


@login_required
def delete_job(request, job_id):
    """Deletes job entry"""
    # Delete job from database if matching id is found.
    try:
        request.user.job_set.get(id=job_id).delete()
        messages.success(request, "Job Deleted from Job List")
    except Job.DoesNotExist:
        messages.warning(request, "Unable to delete job...")
    finally:
        return redirect("opportunities-jobs")


@login_required
def update_job(request, job_id):
    """Updates Job Entry"""
    context = {"jobs": Job.objects.filter(author=request.user).all()}

    # fetch job object related to passed job_id
    obj = get_object_or_404(Job, id=job_id)

    # update job form
    form = AddJobForm(
        request.POST or None, instance=obj, initial={"author": request.user}
    )
    if form.is_valid():
        form.save()
        messages.success(request, "Job Updated")
        return redirect("opportunities-jobs")
    context["form"] = form

    return render(request, "opportunities/jobs-update.j2", context)


@login_required
def skills(request):
    """Renders skills for the logged in user"""
    context = {
        "skills": Skills.objects.filter(user=request.user).all().order_by("name")
    }

    # add a skill
    form = AddSkillForm(request.POST or None, initial={"user": request.user})
    if form.is_valid():
        messages.success(request, "Congrats on learning a new skill")
        form.save()
        return redirect("opportunities-skills")

    context["form"] = form

    return render(request, "opportunities/skills.j2", context)


@login_required
def delete_skill(request, skills_id):
    """Deletes a skill"""
    skill = get_object_or_404(Skills, id=skills_id)
    skill.delete()
    messages.success(request, "Skill has been removed")
    return redirect("opportunities-skills")


@login_required
def dashboard(request):
    """Renders user's dashboard"""
    return render(request, "opportunities/dashboard.j2")


@login_required
def contacts(request):
    """Renders all contacts for a logged in user"""
    context = {
        "contacts": Contacts.objects.filter(user=request.user)
        .all()
        .order_by("company_name")
    }

    # create new contact
    form = AddContactForm(request.POST or None, initial={"user": request.user})
    if form.is_valid():
        messages.success(request, "Successfully grew your network!")
        form.save()
    context["form"] = form

    return render(request, "opportunities/contacts.j2", context)


@login_required
def update_contact(request, contacts_id):
    """Updates Job Entry"""
    context = {"contacts": Contacts.objects.filter(user=request.user).all()}

    # get details for contact being updated
    obj = get_object_or_404(Contacts, id=contacts_id)

    # update contact form
    form = AddContactForm(
        request.POST or None, instance=obj, initial={"user": request.user}
    )
    if form.is_valid():
        form.save()
        messages.success(request, "Contact updated")
        return redirect("opportunities-contacts")
    context["form"] = form

    return render(request, "opportunities/update-contact.j2", context)


@login_required
def delete_contact(request, contacts_id):
    """Deletes a contact"""
    contact = get_object_or_404(Contacts, id=contacts_id)
    contact.delete()
    messages.success(request, "Contact removed from your network")
    return redirect("opportunities-contacts")



