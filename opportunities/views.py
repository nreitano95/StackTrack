from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator

# from .models import <name of model class here>
from .models import Job, Skills
from .forms import AddJobForm, AddSkillForm
import requests
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def home(request):
    """Renders the Home page if not logged in and user's dashboard if logged in"""
    if request.user.is_authenticated:
        jobs = {"jobs": Job.objects.filter(author=request.user).all()}
        return render(request, "opportunities/dashboard.j2", jobs)
    return render(request, "opportunities/home.j2")


def about(request):
    """Renders the About page"""
    return render(request, "opportunities/about.j2", {"title": "About"})


@login_required
def jobs(request):
    """Renders the Jobs page"""
    context = {"jobs": Job.objects.filter(author=request.user).all()}

    # add job form
    form = AddJobForm(request.POST or None, initial={"author": request.user})
    if form.is_valid():
        messages.success(request, "Job Created")
        form.save()
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
    """Renders all skills"""
    context = {"skills": Skills.objects.all()}

    # add a skill
    form = AddSkillForm(request.POST or None)
    if form.is_valid():
        messages.success(request, "Thanks for contributing to our skills database")
        form.save()
    context["form"] = form

    return render(request, "opportunities/skills.j2", context)


@login_required
def dashboard(request):
    """Renders user's dashboard"""
    return render(request, "opportunities/dashboard.j2")
