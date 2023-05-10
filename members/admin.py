from django.contrib import admin
from .models import Men_Shirt, Men,Men_Jacket,Men_Pants

class MenShirtAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
class MenJacketAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
class MenPantsAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
admin.site.register(Men_Shirt,MenShirtAdmin)
admin.site.register(Men_Jacket,MenJacketAdmin)
admin.site.register(Men_Pants,MenPantsAdmin)
admin.site.register(Men)

# Register your models here.
