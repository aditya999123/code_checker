from django.shortcuts import render
from .models import *
# Create your views here.
def group_problems(request):
	
	row="""<tr><td style="text-align:center;">%s</td><td style="text-align:center;">%s</td><td style="text-align:center;">%s</td></tr>"""
	problem_rows=''
	for o in problems.objects.filter(group=group.objects.get(id=int(request.GET.get('group_id')))):
		count=0
		try:

			count=best_submission.objects.filter(problem_code=o.problem_code).count()

		except Exception,e:
			print e
		print o.title,o.problem_code,count
		problem_rows+=row % (o.title,o.problem_code,count)
		print"here@y"
	return render(request,'group_problems.html',{'problem_rows':problem_rows})
