from django.contrib import admin

from pingaroo.models import MonitorTarget, MonitorResult, User

class MonitorTargetAdmin(admin.ModelAdmin):
    pass

class MonitorResultAdmin(admin.ModelAdmin):
    pass

class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(MonitorTarget, MonitorTargetAdmin)
admin.site.register(MonitorResult, MonitorResultAdmin)
admin.site.register(User, UserAdmin)