from django.contrib import admin
from bug.models import bugModel
# Register your models here.
class bugModelAdmin(admin.ModelAdmin):
    list_display = ('description', 'bug_type', 'report_date', 'status')

admin.site.register(bugModel, bugModelAdmin)    