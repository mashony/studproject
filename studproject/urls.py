from django.conf.urls import patterns, include
from django.contrib import admin
admin.autodiscover()
from django.contrib.auth.views import login,logout
from django.conf import settings

urlpatterns = patterns('app.views',
    (r'^$','index'),
    (r'^students/$','studs'),
    (r'^groups/$','groups'),

    (r"^student/add","stud_add"),
    (r"^student/(?P<stud_id>\d+)/delete/$","stud_del"),
    (r"^student/(?P<stud_id>\d+)/edit/$","stud_edit"),

    (r"^group/(?P<group_id>\d+)/edit/$","group_edit"),
    (r"^group/(?P<group_id>\d+)/delete/$","group_del"),
    (r"^group/add/$","group_add"),
    (r'^group/(?P<group_id>\d+)/students',"students_of_group"),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('app.auth.views',
    (r"^login/$", "login"),
    (r"^logout/$", "logout"),
    (r"^singup/$","sing_up"),
    (r'^activateprofile/(?P<activation_key>\w+)/$',"activate"),
    #(r"^email_test/$","email_send_test"),
)
#if settings.DEBUG:
#    urlpatterns+= patterns('',
#        (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'./media/'}),
#    )