from django.db import models
from django.contrib.auth.models import User

class ActivateProfile(models.Model):
    user = models.ForeignKey(User,unique=True,verbose_name="user")
    activation_key = models.CharField(max_length=40,unique=True)
    reg_date = models.DateTimeField(auto_now_add=True)