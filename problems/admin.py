from django.contrib import admin

# Register your models here.
from .models import *


class group_Admin(admin.ModelAdmin):
	list_display=['title','type','created','modified']
admin.site.register(group,group_Admin)

class problems_Admin(admin.ModelAdmin):
	list_display=['title','group','problem_code','created','modified']
admin.site.register(problems,problems_Admin)

class testcase_Admin(admin.ModelAdmin):
	list_display=['problem_code','score','created','modified']
admin.site.register(testcase,testcase_Admin)

class testcase_submission_Admin(admin.ModelAdmin):
	list_display=['submission_id','correct','status','score']
admin.site.register(testcase_submission,testcase_submission_Admin)


class submission_Admin(admin.ModelAdmin):
	list_display=['user','problem_code','time','memory','score','created','modified']
admin.site.register(submission,submission_Admin)

class best_submission_Admin(admin.ModelAdmin):
	list_display=['submission_id','problem_code','user']
admin.site.register(best_submission,best_submission_Admin)
