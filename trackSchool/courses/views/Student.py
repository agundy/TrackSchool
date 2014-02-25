from django.contrib import auth
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from courses.forms import StudentForm, LoginForm
from courses.models import Student


def create_student(request):
    """
    form for creating a new student
    """
    if request.method == 'POST':
        student_form = StudentForm(request.POST)

        if student_form.is_valid():  # Verify form is complete, correct data

            if Student.objects.filter(email=student_form.cleaned_data['email']).len != 0:
            # Make sure email isn't already in use

                clean_form = StudentForm()

                errors = ['Error: Email in use']

                return render_to_response('Student/create_student.html', {'form': clean_form, 'errors': errors})

            else:

                user = User.object.create(student_form.cleaned_data['first_name'],
                                          student_form.cleaned_data['email'],
                                          student_form.cleaned_data['password'])

                user.last_name = student_form.cleaned_data['last_name']

                user.save()

                student = Student(user)

                return render_to_response('Student/create_success.html', {'student': student})

        else:

                return render_to_response('Student/create_student.html', {'form': student_form})

    else:

        student_form = StudentForm()

        return render_to_response('Student/create_student.html', {'form': student_form})


def login(request):
    """
    login a user
    """
    if request.method == 'POST':

        login_form = LoginForm(request.POST, auto_id = "id_login_%s")

        if login_form.is_valid():

          try:

            data = login_form.cleaned_data

            # query for a user via email
            try:
              user = User.objects.get(email = data['email'])

            except:

                clean_form = LoginForm()

                errors = ['Error: Email not registered']

                return render_to_response('Student/login.html', {'form': clean_form, 'errors': errors})


            # authenticate that user
            user = auth.authenticate(username = user.username,
                                     password = data['password'])

            # if the password is incorrect, redireect to the login page
            if user is None:

                errors = ['Error: Invalid Password']

                clean_form = LoginForm()

                return render_to_response('Student/login.html', {'form': clean_form, 'errors': errors})

            # otherwise, log the user in
            auth.login(request, user)

            return render_to_response('Student/login_success.html', {})  # This will be replaced with a redirect to dashboard

          except LoginError as e:
            pass
          except:
            raise

        else:

            clean_form = LoginForm()

            errors = ['']

            return render_to_response('Student/login.html', {'form': clean_form, 'errors': errors})

    else:

        login_form = LoginForm()

        errors = []

        return render_to_response('Student/login.html', {'form': login_form, 'errors': errors})