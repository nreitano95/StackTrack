from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Constants
EMPLOYMENT_CHOICES = (
    ("Full-Time", "Full-Time"),
    ("Part-Time", "Part-Time"),
    ("Internship", "Internship"),
)

APPLICATION_STATUS_CHOICES = (
    ("Applied", "Applied"),
    ("Interviewing", "Interviewing"),
    ("Rejected", "Rejected"),
    ("Received Offer", "Received Offer"),
)


class Skills(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"


class Job(models.Model):
    # each job is related to only one user. If User deleted, cascade delete Job
    author = models.ForeignKey(User, on_delete=CASCADE)
    company = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=255, choices=EMPLOYMENT_CHOICES)
    salary = models.IntegerField(default=0)
    description = models.TextField()
    application_status = models.CharField(max_length=128, choices=APPLICATION_STATUS_CHOICES)
    application_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    # many-to-many relationship with skills
    skills = models.ManyToManyField(Skills)

    # define method, what to display on print
    def __str__(self) -> str:
        return f"{self.title}|{self.company}"


class Contacts(models.Model):
    # all contacts are related to a user
    user = models.ForeignKey(User, on_delete=CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.first_name}|{self.last_name}"
