from django.conf.urls import patterns, include
from django.contrib import admin
admin.autodiscover()

from django.conf import settings

urlpatterns = patterns('app.views',
    (r'^$','index'),
    (r'^students/$','studs'),
    (r'^groups/$','groups'),
    (r'^group/(?P<group_id>\d+)/',"students_of_group"),

    (r"^editform/student/(?P<stud_id>\d+)$","stud_editform"),
    (r"^deleteform/student/(?P<stud_id>\d+)$","stud_delform"),
    (r"^student/add","stud_add"),

    (r"^delete/student/(?P<stud_id>\d+)$","stud_del"),
    #(r"^add/student/$","stud_add"),
    (r"^edit/student/(?P<stud_id>\d+)$","stud_edit"),

    (r"^group/(?P<group_id>\d+)/edit$","group_editform"),
    (r"^group/(?P<group_id>\d+)/delete$","group_delform"),
    (r"^group/add/$","group_addform"),

    (r"^group/add/success$","group_add"),
    (r"^group/(?P<group_id>\d+)/delete/success$","group_del"),
    (r"^group/(?P<group_id>\d+)/edit/success$","group_edit"),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)

#if settings.DEBUG:
#    urlpatterns+= patterns('',
#        (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'./media/'}),
#    )