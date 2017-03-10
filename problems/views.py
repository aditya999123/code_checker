from django.shortcuts import render
from .models import *
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from home.views import nav
from home.models import *
permitted_languages = ["C", "CPP", "CSHARP", "CLOJURE", "CSS", "HASKELL", "JAVA", "JAVASCRIPT", "OBJECTIVEC", "PERL", "PHP", "PYTHON", "R", "RUBY", "RUST", "SCALA"]


@login_required
def check_access(request,submission_id):
	submission_row=submission.objects.get(id=int(submission_id))
	
	flag=False
	if(submission_row.user==str(request.user)):
		flag=True
	else:
		if(submission_row.problem_code.group.open_submissions_to_all==True):
			flag=True
		else:
			flag=False
		if(user_data.objects.get(username=str(request.user)).type=='ADMIN'):
			flag=True
	print "flag",flag
	return flag
@login_required
def problem_submissions(request,problem_code):
	json_nav=nav(request)
	#problem_code= request.GET.get('problem_code')
	print problem_code

	table_row="""<tr>
	<td style="text-align: center;"><a href="/problem/%s">%s</a></td>
	<td style="text-align: center;">%s</td>
		<td style="text-align: center;">%s</td>
	<td style="text-align: center;">%s</td>
	<td style="text-align: center;">%s</td>
	<td style="text-align: center;">%s</td>
	<td style="text-align: center;"><button type="button" class="btn btn-success" onclick="window.location='/submission/%s'" %s>View</button>
	</td></tr>"""
	table=""
	problem_row=problems.objects.get(problem_code=problem_code)
	for o in submission.objects.filter(problem_code=problem_row).order_by('created').reverse():
		if (check_access(request,o.id)==True):
			table+=table_row%(o.problem_code,o.problem_code,o.user,str(o.created)[:19],o.time,o.memory,o.score,o.id,'enabled')
		else:
			table+=table_row%(o.problem_code,o.problem_code,o.user,str(o.created)[:19],o.time,o.memory,o.score,o.id,'disabled')
	json_nav['table']=table

	return render(request,'submissions.html',json_nav)

@login_required
def user_submissions(request,username):
	json_nav=nav(request)
	problem_code= request.GET.get('problem_code')

	table_row="""<tr>
	<td style="text-align: center;"><a href="/problem/%s">%s</a></td>
	<td style="text-align: center;">%s</td>
	<td style="text-align: center;">%s</td>
		<td style="text-align: center;">%s</td>
	<td style="text-align: center;">%s</td>
	<td style="text-align: center;">%s</td>
	<td style="text-align: center;"><button type="button" class="btn btn-success" onclick="window.location='/submission/%s'" %s>View</button>
	</td></tr>"""
	table=""
	if(problem_code==None):
		for o in submission.objects.filter(user=str(request.user)).order_by('created').reverse():
			if (check_access(request,o.id)==True):
				table+=table_row%(o.problem_code,o.problem_code,o.user,str(o.created)[:19],o.time,o.memory,o.score,o.id,'enabled')
			else:
				table+=table_row%(o.problem_code,o.problem_code,o.user,str(o.created)[:19],o.time,o.memory,o.score,o.id,'disabled')
	else:
		problem_row=problems.objects.get(problem_code=problem_code)
		for o in submission.objects.filter(user=str(request.user),problem_code=problem_row).order_by('created').reverse():
			if (check_access(request,o.id)==True):
				table+=table_row%(o.problem_code,o.problem_code,o.user,str(o.created)[:19],o.time,o.memory,o.score,o.id,'enabled')
			else:
				table+=table_row%(o.problem_code,o.problem_code,o.user,str(o.created)[:19],o.time,o.memory,o.score,o.id,'disabled')
	json_nav['table']=table

	return render(request,'submissions.html',json_nav)

@login_required
def show_testcases(request,submission_id):
	flag=check_access(request,submission_id)
	json_nav=nav(request)
	submission_row=submission.objects.get(id=int(submission_id))
	if(flag==True):
		red='#FF8160'
		green='#0CCE6B'
		testcase_row=""" <div class="panel panel-default" style="background:%s;text-align: center">
		<div class="panel-body" >
		<div class="col-sm-4">%s</div><div class="col-sm-4">%s</div><div class="col-sm-4">%s</div></div>
		</div>"""
		table=""
		i=0
		for o in testcase_submission.objects.filter(submission_id=submission_row):
			i+=1
			if(o.correct==True):
				table+=testcase_row%(green,i,o.status,o.score)
			else:
				table+=testcase_row%(red,i,o.status,o.score)

		json_nav['table']=table
		json_nav['problem_code']=submission_row.problem_code
		json_nav['code']=submission_row.code
		return render(request,'section.html',json_nav)
	if(flag==False):
		json_nav['error']='Acess Denied'
		return render(request,'error.html',json_nav)
@login_required
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

@login_required
def problem(request,problem_code):
	
	problem_row=problems.objects.get(problem_code=problem_code)

	json_nav=nav(request)
	json_nav['title']=str(problem_row.title)
	json_nav['problem_code']=str(problem_row.problem_code)
	json_nav['question']=str(problem_row.question)
	json_nav['constraints']=str(problem_row.constraints)
	json_nav['example']=str(problem_row.example)
	
	return render(request,'problem.html',json_nav)
import requests
RUN_URL = "https://api.hackerearth.com/v3/code/run/"


def runCode(problem_code,code,lang,input,time_limit):

	run_data = {
	'client_secret': '2e8285e5eb07253a012aad6d9823722b3548e249',
	'async': 0,
	'source': code,
	'lang': lang,
	'time_limit': time_limit,
	'memory_limit': 262144,
	}


	code_input = ""
	run_data['input'] = input
	code_input = run_data['input']

	"""
	Make call to /run/ endpoint of HackerEarth API
	and save code and result in database
	"""
	r = requests.post(RUN_URL, data=run_data,verify=False)
	r = r.json()
	print r
	return r 
@login_required
def submit_api(request,problem_code,code,lang):
	
	problem_row=problems.objects.get(problem_code=problem_code)
	submission_row=submission.objects.create(problem_code=problem_row,user=str(request.user),code=code)
	score=0
	time=0
	memory=0
	flag=1
	print"@75"
	for o in testcase.objects.filter(problem_code=problem_row):
		print"@76"
		response=runCode(problem_code,code,lang,o.input,o.time_limit)
		print"@returned at 77"
		testcase_row=testcase_submission.objects.create(submission_id=submission_row)
		print response['compile_status']
		if(response['compile_status']=='OK'):
			print response['run_status']['status']
			if(response['run_status']['status']=='AC'):
				print "a=",o.expected_output
				print "b=",response['run_status']['output']
				if(o.expected_output==response['run_status']['output'] or o.expected_output+'\n'==response['run_status']['output']):
					print"here@87"
					testcase_row.status='AC'
					testcase_row.correct=True
					testcase_row.score=o.score
					testcase_row.save()
					score+=o.score
					if(response['run_status']['time_used']>time):
						time=response['run_status']['time_used']
					if(response['run_status']['memory_used']>memory):
						memory=response['run_status']['memory_used']
				else:
					print"here@99"
					testcase_row.status='WA'
					testcase_row.correct=False
					testcase_row.score=0
					testcase_row.save()
			else:
				testcase_row.status=response['run_status']['status']
				testcase_row.correct=False
				testcase_row.score=0
				testcase_row.save()
		else:
			testcase_row.status='CE'
			testcase_row.correct=False
			testcase_row.score=0
			testcase_row.save()

	print"@117"
	submission_row.score=score
	submission_row.time=time
	submission_row.memory=memory
	submission_row.save()
	print"@122"
	best_submission_row,created=best_submission.objects.get_or_create(user=user_data.objects.get(username=str(request.user)),problem_code=problem_row)
	print"@124"
	if(created==False):
		print"@126"
		best_submission_old=best_submission_row.submission_id
		print"@128"		
		if(submission_row.score>best_submission_old.score):
			print"@130"
			best_submission_row.submission_id=submission_row
		if(submission_row.score==best_submission_old):
			if(submission_row.time<best_submission_old.time):
				best_submission_row.submission_id=submission_row
			if(submission_row.time==best_submission_old.time):
				if(submission_row.memory<best_submission_old.memory):
					best_submission_row.submission_id=submission_row
	if(created==True):
		best_submission_row.submission_id=submission_row

	best_submission_row.save()

	return submission_row.id


def check_active(problem_code):
	print"@128............................."
	group_row=problems.objects.get(problem_code=problem_code).group
	print"@130............................."

	return group_row.active

@login_required
def submit(request,problem_code):
	json_nav=nav(request)
	if(request.method=="GET"):
		print"@139............................."
		if(check_active(problem_code)==True):
			print"@141............................."
			return render(request,'submit.html')
		else:
			json_nav['error']='contest has ended'
			return render(request,'error.html',json_nav)
	if(request.method=='POST'):

		if(check_active(problem_code)==True):
			code = request.POST.get('source')
			print str(code)
			lang = request.POST.get('lang')
			if(code!=None):
				if lang in permitted_languages:
					print"@153"
					submission_id=submit_api(request,problem_code,code,lang)
					print"@155"
					return HttpResponseRedirect('/submission/'+str(submission_id))
				else:
					json_nav['error']='langauge not supported'
					return render(request,'error.html',json_nav)
			else:
				json_nav['error']='source cannot be empty'
				return render(request,'error.html',json_nav)


		else:
			json_nav['error']='contest has ended'
			return render(request,'error.html',json_nav)