from django.conf.urls import patterns, include, url
from views import *
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns(
    '',
    #Beta Sign up
    url(r'^request-beta', Student.request_beta),

    # Student
    url(r'^student/create', Student.create_student),
    url(r'^student/join_school/$', Student.join_school),
    url(r'^student/dashboard', Student.show_dashboard),
    url(r'^confirm_email/(?P<confirmation_code>\w{0,50})/(?P<username>\w{0,50})/$',
        Student.confirm_edu_email),
    url(r'^accounts/login', Student.login),
    url(r'^accounts/logout', Student.logout),
    url(r'^student/profile/(\d+)$', Student.profile),
    url(r'^student/groups/', Student.show_student_groups),
    url(r'^student/grades/', Student.show_grades),
    url(r'^student/js_grades/', Student.js_grades),
    url(r'^student/edit/', Student.student_edit),
    url(r'^student/assignment/add/(\d+)$', Student.add_student_item),
    url(r'^student/assignment/remove/(\d+)$', Student.remove_student_item),
    url(r'^student/assignment/edit/(\d+)$', Student.edit_student_item),
    url(r'^student/assignment_type/add/(\d+)$', Student.assignment_type_add),
    url(r'^student/assignment_type/edit/(\d+)$', Student.assignment_type_edit),
    url(r'^forgot-password/', Student.forgot_password),
    # Course
    url(r'^course/create', Course.create_course),
    url(r'^course/students_courses', Course.show_student_courses),
    url(r'^course/browse', Course.browse_courses),
    url(r'^course/profile/(\d+)$', Course.profile),
    url(r'^course/section/join/(\d+)$', Course.join_section),
    url(r'^course/section/leave/(\d+)$', Course.leave_section),
    url(r'^course/section/add_assignment/(\d+)$', Course.add_assignment),
    url(r'^course/section/add/(?P<course>\w{0,50})$', Course.add_section),
    url(r'^course/section/show/(\d+)$', Course.show_section),
    # REST API
    url(r'^rest/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest/schools/$', API.SchoolList.as_view()),
    url(r'^rest/schools/(?P<pk>[0-9]+)/$', API.SchoolDetail.as_view()),
    url(r'^rest/students/$', API.StudentList.as_view()),
    url(r'^rest/students/(?P<pk>[0-9]+)/$', API.StudentDetail.as_view()),
    url(r'^rest/schools/(?P<schoolPk>[0-9]+)/courses/$', API.CourseList.as_view()),
    url(r'^rest/schools/(?P<schoolPk>[0-9]+)/courses/(?P<pk>[0-9]+)/$', API.CourseDetail.as_view()),
    url(r'^rest/schools/(?P<schoolPk>[0-9]+)/courses/(?P<coursePk>[0-9]+)/sections/$', API.SectionList.as_view()),
    url(r'^rest/schools/(?P<schoolPk>[0-9]+)/courses/(?P<coursePk>[0-9]+)/sections/(?P<pk>[0-9]+)/$',
        API.SectionDetail.as_view())

)

urlpatterns = format_suffix_patterns(urlpatterns)
