from models import Student,Group,get_students_of_group
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import StudForm,GroupForm
from datetime import datetime

def index(request):
    return render_to_response("one.html")

def studs(request):
    return render_to_response("students.html",
            {'stud_list':Student.objects.all()})

def groups(request):
    return render_to_response("groups.html",
            {'groups_list':Group.objects.all(),
             "students":Student.objects.all()})

def students_of_group(request,group_id):
    return render_to_response("students.html",
            {'stud_list':get_students_of_group(group_id)})

def stud_addform(request):
    return render_to_response("admin/stud_addform.html",
            {'group_list':Group.objects.all(),
             'form':StudForm()},
            context_instance=RequestContext(request))

def stud_editform(request,stud_id):
    return render_to_response("admin/stud_editform.html",
            {'student':Student.objects.get(id=stud_id),
             'group_list':Group.objects.all()},
            context_instance=RequestContext(request))

def stud_delform(request,stud_id):
    return render_to_response("admin/stud_delform.html",
            {'student':Student.objects.get(id=stud_id)})

def stud_add(request):
    gr = Group.objects.get(id=request.POST['group'])
    try:
        date = datetime.strptime(request.POST["date_of_birth"],"%d.%m.%Y")
    except ValueError:
        print "Something wrong with dateformat"
    st = Student(first_name=request.POST["first_name"],
            second_name=request.POST['second_name'],
            patronymic=request.POST['patronymic'],
            date_of_birth=date,
            group=gr)
    st.save()
    return HttpResponseRedirect("/students")

def stud_edit(request,stud_id):
    try:
        date = datetime.strptime(request.POST["date_of_birth"],"%d.%m.%Y")
    except ValueError:
        print "Something wrong with dateformat"
    Student(id=stud_id,
        first_name=request.POST["first_name"],
        second_name=request.POST['second_name'],
        patronymic=request.POST['patronymic'],
        date_of_birth=date,
        group=Group.objects.get(id=request.POST['group'])).save()
    return HttpResponseRedirect("/students")

def stud_del(request,stud_id):
    Student.objects.get(id=stud_id).delete()
    return HttpResponseRedirect("/students")


def group_addform(request):
    return render_to_response("admin/group_add_form.html",
            {'form':GroupForm},context_instance=RequestContext(request) )

def group_delform(request,group_id):
    return render_to_response("admin/group_del_form.html",
            {"group":Group.objects.get(id=group_id)},
            context_instance=RequestContext(request))

def group_editform(request,group_id):
    return render_to_response("admin/group_edit_form.html",
        {"group":Group.objects.get(id=group_id),
         "stud_list":Student.objects.all()},
         context_instance=RequestContext(request))


def group_del(request,group_id) :
    Group.objects.get(id=group_id).delete()
    return HttpResponseRedirect("/groups")

def group_edit(request,group_id):
    Group(id=group_id,
        name=request.POST["name"],
        warden=Student.objects.get(id=request.POST["warden"])).save()
    return HttpResponseRedirect("/groups")

def group_add(request):
    student = Student.objects.get(id=request.POST["warden"])
    Group(name=request.POST["name"],warden=student).save()
    return HttpResponseRedirect("/groups")
