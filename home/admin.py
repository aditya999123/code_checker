from django.contrib import admin

# Register your models here.
from .models import *

class KEYS_List_Admin(admin.ModelAdmin):
	list_display=['key','created','modified']
admin.site.register(KEYS_List,KEYS_List_Admin)

class KEYS_internal_Admin(admin.ModelAdmin):
	list_display=['key','value','created','modified']
admin.site.register(KEYS_internal,KEYS_internal_Admin)

class KEYS_external_Admin(admin.ModelAdmin):
	list_display=['key','value','created','modified']
admin.site.register(KEYS_external,KEYS_external_Admin)