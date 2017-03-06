from django.contrib import admin

# Register your models here.
from .models import *


class topics_Admin(admin.ModelAdmin):
	list_display=['title','created','modified']
admin.site.register(topics,topics_Admin)

class problems_Admin(admin.ModelAdmin):
	list_display=['topic','problem_code','created','modified']
admin.site.register(problems,problems_Admin)

class testcase_Admin(admin.ModelAdmin):
	list_display=['problem_code','score','created','modified']
admin.site.register(testcase,testcase_Admin)