from django.db import models
from django.contrib.contenttypes.models import ContentType

class Group(models.Model):
    name = models.CharField(max_length=15,unique=True)
    warden = models.ForeignKey("Student",null=True,blank=True,
        related_name="group_warden")

    def __unicode__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=35)
    patronymic = models.CharField(max_length=25,null=True,blank=True)
    date_of_birth = models.DateField()
    group = models.ForeignKey("Group",on_delete=models.PROTECT)

    def __unicode__(self):
        return "%s %s" % (self.second_name,self.first_name)

def get_students_of_group(group_id):
    try:
        students =  Student.objects.get_query_set().filter(group_id__exact=group_id)
    except Student.DoesNotExist:
        return None
    return students

def save_handler(sender, **kwargs):
    print "PreSave " + sender.__name__
def delete_handler(sender, **kwargs):
    print "PreDelete"


def find_models():
    models = []
    for ct in ContentType.objects.all():
        if ct.model_class().__module__ in ['app.auth.models',
                                           'django.contrib.auth.models',
                                           'app.models']:
            models.append(ct.model_class())
    return models

for model in find_models():
    models.signals.post_save.connect(save_handler,sender=model)
    models.signals.pre_delete.connect(delete_handler,sender=model)