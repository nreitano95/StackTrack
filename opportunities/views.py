from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator

# from .models import <name of model class here>
from .models import Job, Skills
from .forms import AddJobForm
import requests
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def home(request):
    """Renders the Home page"""

    return render(request, "opportunities/home.j2")


def about(request):
    """Renders the About page"""
    return render(request, "opportunities/about.j2", {"title": "About"})


@login_required
def jobs(request):
    """Renders the Jobs page"""
    context = {"jobs": Job.objects.filter(author=request.user).all()}

    # add job form
    form = AddJobForm(request.POST or None, initial={'author':request.user})
    if form.is_valid():
        form.save()
    context['form'] = form

    return render(request, "opportunities/jobs.j2", context)


@login_required
def delete_job(request, job_id):
    """Deletes job entry"""
    # Delete job from database if matching id is found.
    try:
        request.user.job_set.get(id=job_id).delete()
        # User_Favorites.objects.get(ukey=ukey).delete()
        messages.success(request, "Job Deleted from Job List")
    except Job.DoesNotExist:
        messages.warning(request, "Unable to delete job...")
    finally:
        return redirect("opportunities-jobs")


def internships(request):
    """Renders the Internships page"""

    return render(request, "opportunities/internships.j2")


def skills(request):
    """Renders a user's skills"""
    context = {"skills": Skills.objects.all()}
    return render(request, "opportunities/skills.j2", context)
