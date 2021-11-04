from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="opportunities-home"),
    path("about/", views.about, name="opportunities-about"),
    path("jobs/", views.jobs, name="opportunities-jobs"),
    path(
        "jobs/<str:job_id>/delete/", views.delete_job, name="opportunities-delete-job"
    ),
    path(
        "jobs/<str:job_id>/update/", views.update_job, name="opportunities-update-job"
    ),
    path("skills/", views.skills, name="opportunities-skills"),
    path(
        "skills/<int:skills_id>/delete/",
        views.delete_skill,
        name="opportunities-delete-skill",
    ),
    path("dashboard/", views.dashboard, name="opportunities-dashboard"),
]
