from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator

# from .models import <name of model class here>
from .models import Job, Skills
import requests
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def home(request):
    """Renders the Home page"""
    if request.user.is_authenticated:
        return render(request, "opportunities/dashboard.j2")
    return render(request, "opportunities/home.j2")


def about(request):
    """Renders the About page"""
    return render(request, "opportunities/about.j2", {"title": "About"})


def jobs(request):
    """Renders the Jobs page"""
    context = {"jobs": Job.objects.all()}
    return render(request, "opportunities/jobs.j2", context)


def internships(request):
    """Renders the Internships page"""

    return render(request, "opportunities/internships.j2")


def skills(request):
    """Renders a user's skills"""
    context = {"skills": Skills.objects.all()}
    return render(request, "opportunities/skills.j2", context)


@login_required
def dashboard(request):
    """Renders user's dashboard"""
    return render(request, "opportunities/dashboard.j2")