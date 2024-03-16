from django.contrib import admin
from django.contrib.auth.models import Group
from .models import userreg
from .models import companyreg,job,application,notification


class UserRegAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact', 'file', 'username', 'status')
    readonly_fields = ('name', 'email', 'contact', 'file','username')
    exclude = ('password',)  # Exclude the 'password' field from the change form

    def has_add_permission(self, request):
        # Allow adding new objects
        return True

    def has_change_permission(self, request, obj=None):
        # Allow changing existing objects
        return True

    def has_delete_permission(self, request, obj=None):
        # Allow deleting existing objects
        return True



class CompanyRegAdmin(admin.ModelAdmin):
    list_display = ('companyname', 'address', 'email', 'contact', 'username', 'status')
    readonly_fields = ('companyname', 'address', 'email', 'contact','username')
    exclude = ('password',)  # Exclude the 'password' field from the change form

    def has_add_permission(self, request):
        # Allow adding new objects
        return True

    def has_change_permission(self, request, obj=None):
        # Allow changing existing objects
        return True

    def has_delete_permission(self, request, obj=None):
        # Allow deleting existing objects
        return True

class JobAdmin(admin.ModelAdmin):
    list_display = ('company_id', 'job_name', 'job_description')
    readonly_fields = ('company_id','job_name', 'job_description')

    def has_add_permission(self, request):
        # Allow adding new objects
        return True

    def has_change_permission(self, request, obj=None):
        # Allow changing existing objects
        return True

    def has_delete_permission(self, request, obj=None):
        # Allow deleting existing objects
        return True
    


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'job', 'application_date', 'display_status')
    readonly_fields = ('user_id', 'job', 'application_date', 'status')

    def display_status(self, obj):
        return dict(application.status_choice).get(obj.status, obj.status)
    display_status.short_description = 'Status'

    def has_add_permission(self, request):
        # Allow adding new objects
        return True

    def has_change_permission(self, request, obj=None):
        # Allow changing existing objects
        return True

    def has_delete_permission(self, request, obj=None):
        # Allow deleting existing objects
        return True
    

admin.site.unregister(Group)


admin.site.register(userreg,UserRegAdmin)
admin.site.register(companyreg,CompanyRegAdmin)
admin.site.register(job,JobAdmin)
admin.site.register(application,ApplicationAdmin)
admin.site.register(notification)

admin.site.site_header= 'CAREER VISTA'
