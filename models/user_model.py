from django.db import models
import uuid
import datetime

class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    full_name = models.CharField(max_length=150)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=150)
    profile_pic = models.CharField(max_length=550, default="")
    status = models.CharField(max_length=150, default="active")
    designation = models.CharField(max_length=150, default="")
    department = models.CharField(max_length=150, default="")
    gender = models.CharField(max_length=10, required=True)
    created_time = models.DateTimeField(default=datetime.datetime.now())
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    access_level = models.CharField(max_length=150, required=True)
    emp_id = models.CharField(max_length=150, required=True)
    admin_id = models.CharField(max_length=150, required=True)
    access_given_by = models.CharField(max_length=150, required=True)
    user_role = models.CharField(max_length=150, required=True)
    last_modified_time = models.DateTimeField(default=datetime.datetime.now())

class UserBranch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)

