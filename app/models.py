from django.db import models

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
    return Student.objects.get_query_set().filter(group_id__exact=group_id)

