from django.contrib import admin
from myapp1.models import *
# Register your models here.


class TestsAdmin(admin.ModelAdmin):
    list_display = ['test_id', 'test_name', 'price']


class DoctorsAdmin(admin.ModelAdmin):
    list_display = ['doctor_id', 'name', 'specialization']


admin.site.register(Tests, TestsAdmin)
admin.site.register(Doctors, DoctorsAdmin)
admin.site.register(Consult)
admin.site.register(Patients)
admin.site.register(Performed)
admin.site.register(Records)
