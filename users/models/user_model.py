from django.db import models
import uuid
import datetime
from .common_model import BasicBranch, BasicPhoneDetails, BasicAddress

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
    gender = models.CharField(max_length=10)
    created_time = models.DateTimeField(default=datetime.datetime.now())
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    access_level = models.CharField(max_length=150)
    emp_id = models.CharField(max_length=150)
    admin_id = models.CharField(max_length=150)
    access_given_by = models.CharField(max_length=150)
    user_role = models.CharField(max_length=150)
    last_modified_time = models.DateTimeField(default=datetime.datetime.now())
    branch = models.ForeignKey(BasicBranch, on_delete=models.CASCADE)
    address = models.ManyToManyField(BasicAddress)
    phone_no = models.ForeignKey(BasicPhoneDetails, on_delete=models.CASCADE)

    class Meta:
        db_table = "scm_users"
