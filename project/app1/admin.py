from django.contrib import admin

from .models import userreg
from .models import companyreg,job,application,notification


class UserRegAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact', 'file', 'username', 'status')
    fields = ('name', 'email', 'contact', 'file', 'username', 'status')



class CompanyRegAdmin(admin.ModelAdmin):
    list_display = ('companyname', 'address', 'email', 'contact', 'username', 'status')
    fields = ('companyname', 'address', 'email', 'contact', 'username', 'status')


class JobAdmin(admin.ModelAdmin):
    list_display = ('company_id','job_name','job_description')
    fields = ('company_id','job_name','job_description')
    


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'job', 'application_date', 'status')
    fields = ('user_id', 'job', 'application_date', 'status')

admin.site.register(userreg,UserRegAdmin)
admin.site.register(companyreg,CompanyRegAdmin)
admin.site.register(job,JobAdmin)
admin.site.register(application,ApplicationAdmin)
admin.site.register(notification)

