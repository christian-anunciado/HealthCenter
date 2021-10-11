from django.contrib import messages
from django.db.models.query import QuerySet
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import View
from myapp1.models import *

# Create your views here.


class IndexView (View):
    def get(self, request):
        return render(request, 'index.html', {})


class LogInView (View):
    def post(self, request):
        if request.method == 'POST':
            getID = request.POST.get('user')
            check_user_if_exists = Patients.objects.filter(
                patient_id=getID).exists()
            if check_user_if_exists:
                getPassword = request.POST.get('password')
                password_exists = Patients.objects.filter(
                    patient_id=getID).filter(password=getPassword).exists()
                if password_exists:
                    messages.success(self.request, 'Signed in succesfully')
                    return HttpResponseRedirect("/")
                else:   
                    messages.error(self.request, 'Invalid Password!')
                    return redirect('/login')
            else:
                messages.error(self.request, 'User Doest Not Exists!')
                return redirect('/login')

    def get(self, request):
        storage = messages.get_messages(request)
        for _ in storage:
            # This is important
            # Without this loop `_loaded_messages` is empty
            pass
        return render(request, 'login.html', {})


class RegisterView (View):
    def post(self, request):
        if request.method == 'POST':
            patients = Patients()
            patients.patient_id = request.POST.get('patientID')
            patients.name = request.POST.get('name')
            patients.insurance = request.POST.get('Insurance')
            patients.password = request.POST.get('password')
            patients.save()
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
                messages.success(self.request, 'docSuccesful')
                return redirect('/dashboard')
            if request.POST.get('insert') == 'patient':
                pat = Patients()
                pat.patient_id = request.POST.get('id')
                pat.name = request.POST.get('name')
                pat.insurance = request.POST.get('insurance')
                pat.password = request.POST.get('password')
                pat.save()

                messages.success(self.request, 'patSuccesful')
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

            # Delete
            if request.POST.get('delete') == 'patient':
                key = request.POST.get('Pkey')
                delPatient = Patients.objects.get(patient_id = key)
                delPatient.delete()
                messages.success(self.request, 'Deleted Succesfully!')
                return redirect('/dashboard')

    def get(self, request):
        queryDoctor = Doctors.objects.all()
        queryPatients = Patients.objects.all()
        storage = messages.get_messages(request)
        for _ in storage:
            # This is important
            # Without this loop `_loaded_messages` is empty
            pass

        return render(request, 'dashboard.html', {'queryDoctor': queryDoctor, 'queryPatients': queryPatients})
