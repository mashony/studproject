import re
import hashlib
import time
from datetime import datetime

from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import AuthenticationForm
from app.auth.forms import AuthorizationForm
from app.auth.models import ActivateProfile
from django.template.loader import render_to_string
from django.conf import settings
from django.core import mail

SHA1_RE = re.compile('^[a-f0-9]{40}$')

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            print "user_login"
            return HttpResponseRedirect("/")
        else:
            print "error"
            return render_to_response("registration/login.html",
                {"form":AuthenticationForm()},
                context_instance=RequestContext(request))
    else:
        return render_to_response("registration/login.html",
            {"form":AuthenticationForm(),
             "errors":None},
            context_instance=RequestContext(request))

def logout(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    auth.logout(request)
    return HttpResponseRedirect("/")

def sing_up(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    if request.method == "POST":
        if ("email" in request.POST) and ("password" in request.POST):
            form = AuthorizationForm(request.POST)
            if form.is_valid():
                user = User(username=request.POST["login"],
                            first_name=request.POST["first_name"],
                            last_name=request.POST["last_name"],
                            email=request.POST["email"],
                            password=request.POST["password"],
                            is_active=False)
                user.save()
                user.groups.add(Group.objects.get(name=request.POST["role"]))
                activation_key = gen_activation_key(user)
                activate_profile = ActivateProfile(user=user,
                                                   activation_key=activation_key)
                activate_profile.save()
                send_email(activate_profile)
                return HttpResponseRedirect("/")
        return render_to_response("registration/sing_up.html",
            {"form":AuthorizationForm()},
            context_instance=RequestContext(request))
    else:
        return render_to_response("registration/sing_up.html",
            {"form":AuthorizationForm()},
            context_instance=RequestContext(request))

def activate(request,activation_key):
    if SHA1_RE.search(activation_key):
        try:
            activate_profile = \
                ActivateProfile.objects.get(activation_key=activation_key)
        except ActivateProfile.DoesNotExist:
            raise Http404
        if not activate_profile.user.is_active:
            user = activate_profile.user
            user.is_active = True
            user.save()
            activate_profile.save()
            return HttpResponseRedirect("/")
    return render_to_response("error.html",
        {"error","Activation_key didn't find or activated time is over!"})

def change_password(request):
    pass

def edit_user(request):
    pass

def delete_user(request):
    pass

def send_email(activate_profile):
    message = render_to_string('registration/activation_email.html',
        {"username":activate_profile.user.username,
         "activation_key":activate_profile.activation_key})
    email_msg = mail.EmailMessage("Registration on StudProject", message,
        settings.EMAIL_HOST_USER,[activate_profile.user.email])
    email_msg.content_subtype="html"
    email_msg.send()

def gen_activation_key(user):
    username = user.username
    if isinstance(username, unicode):
        username = username.encode('utf-8')
    date_reg = datetime.now()
    salt = "".join([username,user.email,str(time.mktime(date_reg.timetuple()))])
    return hashlib.sha1(salt).hexdigest()



#def email_send_test(request):
#    if request.method == "POST":
#        message = render_to_string('registration/testmail.html')
#        msg = mail.EmailMessage(request.POST["subject"], message,
#            settings.EMAIL_HOST_USER, [request.POST["email"]])
#        msg.content_subtype="html"
#        msg.send()
#        return HttpResponseRedirect("/")
#    return render_to_response("email_test.html",
#        context_instance=RequestContext(request))