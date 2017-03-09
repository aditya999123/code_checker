from django.shortcuts import render
from .models import *
# Create your views here.
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
	return render(request,'group_problems.html',{'problem_rows':problem_rows})


def problem(request,problem_code):
	
	problem_row=problems.objects.get(problem_code=problem_code)
	problem_json={
	'title':problem_row.title,
	'problem_code':problem_row.problem_code,
	'question':problem_row.question,
	'constraints':problem_row.constraints,
	'example':problem_row.example,
	}
	return render(request,'problem.html',problem_json)

def submit(request,problem_code):
	problem_row=problems.objects.get(problem_code=problem_code)