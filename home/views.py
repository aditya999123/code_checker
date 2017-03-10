from django.shortcuts import render
from django.contrib.auth.views import login,logout
from django.http import HttpResponseRedirect, HttpResponse
from problems.models import group,problems
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *
from django.contrib.auth.models import User
def nav(request):
	list1=""
	list2=""
	list3=""
	list4=""

	for o in group.objects.filter(type='CONTEST',active=True):
		if(problems.objects.filter(group=o).count()>0):
			list1+='<li><a href="/group/'+str(o.id)+'">'+o.title+'</a></li>'
	
	for o in group.objects.filter(type='LAB',active=True):
		if(problems.objects.filter(group=o).count()>0):
			list2+='<li><a href="/group/'+str(o.id)+'">'+o.title+'</a></li>'

	
	for o in group.objects.filter(type='PRACTICE',active=True):
		if(problems.objects.filter(group=o).count()>0):
			list3+='<li><a href="/group/'+str(o.id)+'">'+o.title+'</a></li>'

	if request.user.is_authenticated():
		list4+="""  <button class="btn btn-primary dropdown-toggle" type="button" style="width: 100%;text-align:left;" onclick="location.href='/user/"""+str(request.user)+"""/submissions';">MY SUBMISSIONS
  				</button> 
<div style="padding-top: 10px;">
		 <button class="btn btn-primary dropdown-toggle" type="button" style="width: 100%;text-align:left;" onclick="location.href='/logout';">LOGOUT
  				</button>
  				</div>
  				"""
	else:
		list4+="""  				<button class="btn btn-primary dropdown-toggle" type="button" style="width: 100%;text-align:left;" onclick="location.href='/register';">REGISTER
  				</button>    
<div style="padding-top: 10px;">

<button class="btn btn-primary dropdown-toggle" type="button" style="width: 100%;text-align:left;" onclick="location.href='/login';">LOGIN
  				</button>
  				</div>"""
  	return {'list1':list1,'list2':list2,'list3':list3,'list4':list4}

def home(request):
	list1=""
	list2=""
	list3=""
	list4=""

	json_nav=nav(request)

	return render(request,'main.html',json_nav)

def login_check(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home')
    else:
        return login(request)
@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
@login_required
def scribble(request):
	json_nav=nav(request)
	return render(request,'scribble.html',json_nav)

def register(request):
	if(request.method=='GET'):
		return render(request,'registration/register.html')
	else:
		roll=request.POST.get('roll')
		password=request.POST.get('password')
		password2=request.POST.get('password2')
		if(len(roll)<8 or len(password)<6):
			return render(request,'registration/register.html',{'error':"some error occured"})
		try:
			user=user_data.objects.get(username=roll)
			return render(request,'registration/register.html',{'error':"user already exsists"})
		except Exception,e:
			print e
			if(password==password2):
				print roll,password
				user=User.objects.create_user(username=roll,password=password)
				print"y"
				user_data.objects.create(username=roll,type='USER')
				return HttpResponseRedirect('/login')
			else:
				return render(request,'registration/register.html',{'error':"password did not match"})