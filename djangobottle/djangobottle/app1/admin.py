__author__ = 'rohini'

from django.contrib import admin
from djangobottle.app1.models import MoocInstance

class MoocInstanceAdmin(admin.ModelAdmin):
    pass
admin.site.register(MoocInstance, MoocInstanceAdmin)