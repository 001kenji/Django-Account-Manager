from django.contrib import admin
from .models import Teachers
# Register your models here.
admin.site.site_title='log-in page'
admin.site.site_header='LOG-IN'

class TeacherAdmin(admin.ModelAdmin):
    list_display = ("username", "email",'online')
admin.site.register(Teachers,TeacherAdmin)
