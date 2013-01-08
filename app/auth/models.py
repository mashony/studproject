from django.db import models
from django.contrib.auth.models import User

class ActivateProfile(models.Model):
    user = models.ForeignKey(User,unique=True,verbose_name="user")
    activation_key = models.CharField(max_length=40,unique=True)
    reg_date = models.DateTimeField(auto_now_add=True)


# TODO: Myself registration user
#class ProjectUser(models.Model):
#    user = models.OneToOneField(User)
#    date_of_birth = models.DateField()

#    def __uncode__(self):
#        return self.user.username

#def create_project_user_callback(sender,instance, **kwargs):
#    project_user, new = ProjectUser.objects.get_or_create(user=instance)
#models.signals.post_save(create_project_user_callback,User)