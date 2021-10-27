from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="opportunities-home"),
    path("about/", views.about, name="opportunities-about"),
    path("jobs/", views.jobs, name="opportunities-jobs"),
    path("skills/", views.skills, name="opportunities-skills"),
    path("dashboard/", views.dashboard, name="opportunities-dashboard"),
]

