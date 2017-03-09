from django.shortcuts import render
from .models import *
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from home.views import nav
def group_problems(request,group_id):
	
	row="""<tr><td style="text-align:center;"><a href="/problem/%s">%s</a></td>
	<td style="text-align:center;">%s</td>
	<td style="text-align:center;">%s</td></tr>"""
	problem_rows=''
	for o in problems.objects.filter(group=group.objects.get(id=int(group_id))):
		count=0
		try:

			count=best_submission.objects.filter(problem_code=o).count()

		except Exception,e:
			print e
		problem_rows+=row % (o.problem_code,o.title,o.problem_code,count)

	json_nav=nav(request)
	json_nav['problem_rows']=problem_rows
	return render(request,'group_problems.html',json_nav)


def problem(request,problem_code):
	
	problem_row=problems.objects.get(problem_code=problem_code)

	json_nav=nav(request)
	json_nav['title']=str(problem_row.title)
	json_nav['problem_code']=str(problem_row.problem_code)
	json_nav['question']=str(problem_row.question)
	json_nav['constraints']=str(problem_row.constraints)
	json_nav['example']=str(problem_row.example)
	
	return render(request,'problem.html',json_nav)

def submit_api(problem_code):
	pass 

def submit(request,problem_code):

	if(request.method=="GET"):
		if(check_active(problem_code)==True):
			return render(request,'submit.html')
		else:
			return render(request,'ended.html')
	if(request.method=='POST'):
		if(check_active(problem_code)==True):
			submit_api(problem_code)
			return HttpResponseRedirect('/group/')
		else:
			return render(request,'ended.html')

def test(request):
	return render(request,'a.html')