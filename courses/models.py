from django.db import models
from django.contrib.auth.models import User

"""
we have a Subject the contain courses and every course contain modules
    - subject has:
        1. title
        2. slug
            * order by title
    - course has :
        1. owner(a User)
        2. subject(a Subject)
        3. title
        4. slug
        5. overview
        6. created date
            * order by created (des)
    - module has :
        1. course (a course)
        2. title
        3. description 
"""


class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Course(models.Model):
    owner = models.ForeignKey(User, related_name="courses_created", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name="courses", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course, related_name="modules", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

