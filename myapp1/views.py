from django.contrib import messages
from django.db.models.query import QuerySet
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from myapp1.models import *

# Create your views here.


class IndexView (View):
    def post(self, request):
        if request.user.is_authenticated:
            if request.method == 'POST':
                # Get args
                pName = request.POST.get('name')
                pEmail = request.POST.get('email')
                pPhone = request.POST.get('phone')
                cDate = request.POST.get('date')
                testID = request.POST.get('testID')
                department = request.POST.get('department')

                patient = None

                check_patient = Patients.objects.filter(name = pName)

                # Add new Patient if patient does not exists!
                if not check_patient.exists():
                    patient = Patients()
                    patient.name = pName
                    patient.email = pEmail
                    patient.contactno = pPhone
                    patient.save()

                getPatient = Patients.objects.get(name = pName)
                getTest = Tests.objects.get(test_id=testID)
                getDoctor = Doctors.objects.get(doctor_id=department)
                getPerform = Performed.objects.get(result_id = 3)

                consult = Consult()

                consult.date = cDate
                consult.test = getTest
                consult.patient = getPatient
                consult.doctor = getDoctor

                consult.save()

                latest_consultID = Consult.objects.latest('consult_id')
                
                record = Records()

                record.patient = getPatient
                record.doctor = getDoctor
                record.test = getTest
                record.consult = latest_consultID
                record.result = getPerform

                record.save()

                messages.success(self.request, 'Appoinment sent!')
                return HttpResponseRedirect("/")
        else:
            messages.error(self.request, 'You need to log in before making appointment!')
            return HttpResponseRedirect("/")



    def get(self, request):
        storage = messages.get_messages(request)
        for _ in storage:
            # This is important
            # Without this loop `_loaded_messages` is empty
            pass
        return render(request, 'index.html', {})


class LogInView (View):
    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirect to a success page.
                userSession = request.user or "none"
                messages.success(self.request, 'Signed in succesfully')
                return HttpResponseRedirect("/", {'user': userSession})
        
            else:
                # Return an 'invalid login' error message.
                messages.error(self.request, 'Wrong username or password!')
                return redirect('/login')
        

    def get(self, request):
        storage = messages.get_messages(request)
        for _ in storage:
            # This is important
            # Without this loop `_loaded_messages` is empty
            pass
        return render(request, 'login.html', {})

class LogOutView (View):
    def get(self, request):
        logout(request)
        messages.success(self.request, "Logged out!")
        return redirect('/login')

class RegisterView (View):
    def post(self, request):
        if request.method == 'POST':
            # username
            # password
            # email
            # first_name
            # last_name
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')

            user = User.objects.create_user(username, email, password)
            first_name = request.POST.get('fname')
            last_name = request.POST.get('lname')

            user.first_name = first_name
            user.last_name = last_name

            user.save()

            messages.success(self.request, 'Registration Success!')
            return redirect('/register')

    def get(self, request):
        storage = messages.get_messages(request)
        for _ in storage:
            # This is important
            # Without this loop `_loaded_messages` is empty
            pass
        return render(request, 'register.html', {})


class DashBoardView (View):

    def post(self, request):
        if request.method == 'POST':
            # Insert
            if request.POST.get('insert') == 'doctor':
                doc = Doctors()
                doc.doctor_id = request.POST.get('id')
                doc.name = request.POST.get('name')
                doc.specialization = request.POST.get('specialization')
                doc.save()
                messages.success(self.request, 'Added successfully! ')
                return redirect('/dashboard')
            if request.POST.get('insert') == 'patient':
                pat = Patients()
                pat.name = request.POST.get('name')
                pat.insurance = request.POST.get('insurance')
                pat.contactno = request.POST.get('contact')
                pat.save()

                messages.success(self.request, 'Added successfully!')
                return redirect('/dashboard')

            # Edit
            if request.POST.get('edit') == 'patient':
                edit_key = request.POST.get('edit_id')
                editPatient = Patients.objects.get(patient_id = edit_key)
                editPatient.name = request.POST.get('edit_name')
                editPatient.insurance = request.POST.get('edit_insurance')
                editPatient.save()
                messages.success(self.request, 'Edited successfully!')
                return redirect('/dashboard')

            if request.POST.get('edit') == 'doctor':
                edit_key = request.POST.get('edit_id_dcotor')
                editDoctor = Doctors.objects.get(doctor_id = edit_key)
                editDoctor.name = request.POST.get('edit_name_doctor')
                editDoctor.specialization = request.POST.get('edit_specialization')
                editDoctor.save()
                messages.success(self.request, 'Edited successfully!')
                return redirect('/dashboard')
            
            if request.POST.get('edit') == 'records':
                edit_key = request.POST.get('edit_id_records')
                editRecords = Records.objects.get(record_id = edit_key)
                editRecords.result = Performed.objects.get(result_id = request.POST.get('result'))
                
                editRecords.save()
                messages.success(self.request, 'Edited successfully!')
                return redirect('/dashboard')

            # Delete
            if request.POST.get('delete') == 'doctor':
                key = request.POST.get('Dkey')
                delDoctor = Doctors.objects.get(doctor_id = key)
                delDoctor.delete()
                messages.success(self.request, 'Deleted Succesfully!')
                return redirect('/dashboard')

            if request.POST.get('delete') == 'patient':
                key = request.POST.get('Pkey')
                delPatient = Patients.objects.get(patient_id = key)
                delPatient.delete()
                messages.success(self.request, 'Deleted Succesfully!')
                return redirect('/dashboard')

            if request.POST.get('delete') == 'records':
                key = request.POST.get('Rkey')
                delRecrods = Records.objects.get(record_id = key)
                delRecrods.delete()
                messages.success(self.request, 'Deleted Succesfully!')
                return redirect('/dashboard')

    def get(self, request):
        queryDoctor = Doctors.objects.all()
        queryPatients = Patients.objects.all()
        queryRecords = Records.objects.all()
        counterPatients = queryPatients.count()
        counterRecords = queryRecords.count()
        counterConsult = Consult.objects.all().count()
        counterTest = Tests.objects.all().count()

        counterList = [counterPatients,counterConsult,counterTest,counterRecords]

        contexts = {
            'queryPatients': queryPatients, 
            'queryDoctor': queryDoctor, 
            'queryRecords': queryRecords, 
            'counterList': counterList,

        
        }


        storage = messages.get_messages(request)
        for _ in storage:
            # This is important
            # Without this loop `_loaded_messages` is empty
            pass

        return render(request, 'dashboard.html', contexts)
