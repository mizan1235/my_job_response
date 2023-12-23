from django.contrib import admin
from job.models import user_cred,employee_cred,job_details,job_apllicaions
admin.site.register(user_cred)
admin.site.register(employee_cred)
admin.site.register(job_details)

admin.site.register(job_apllicaions)

# Register your models here.
