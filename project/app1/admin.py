from django.contrib import admin

from .models import userreg
from .models import companyreg,job,application,notification



admin.site.register(userreg)
admin.site.register(companyreg)
admin.site.register(job)
admin.site.register(application)
admin.site.register(notification)

