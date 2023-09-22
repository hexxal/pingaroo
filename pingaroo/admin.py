from django.contrib import admin

from pingaroo.models import MonitorTarget, MonitorResult

class MonitorTargetAdmin(admin.ModelAdmin):
    pass

class MonitorResultAdmin(admin.ModelAdmin):
    pass

admin.site.register(MonitorTarget, MonitorTargetAdmin)
admin.site.register(MonitorResult, MonitorResultAdmin)