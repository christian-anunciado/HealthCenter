from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import View
from myapp1.models import *

# Create your views here.


class IndexView (View):
    def get(self, request):
        return render(request, 'index.html', {})


class LogInView (View):
    def get(self, request):
        return render(request, 'login.php', {})


class DashBoardView (View):

    def get(self, request):
        queryDoctor = Doctors.objects.all()
        queryPatients = Patients.objects.all()

        return render(request, 'dashboard.html', {'queryDoctor': queryDoctor, 'queryPatients': queryPatients})
