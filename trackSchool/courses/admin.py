from models import *
from django.contrib import admin
from django.contrib.auth.models import User, Group

for model in (
    School,
    Student,
    Membership,
    Course,
    GradeGroup
):
    admin.site.register(model)
