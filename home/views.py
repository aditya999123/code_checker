from django.shortcuts import render
from django.contrib.auth.views import login,logout
from django.http import HttpResponseRedirect, HttpResponse
from problems.models import group,problems
# Create your views here.

def nav(request):
	list1=""
	list2=""
	list3=""
	list4=""

	for o in group.objects.filter(type='CONTEST',active=True):
		if(problems.objects.filter(group=o).count()>0):
			list1+='<li><a href="/problems?group_id='+str(o.id)+'">'+o.title+'</a></li>'
	
	for o in group.objects.filter(type='LAB',active=True):
		if(problems.objects.filter(group=o).count()>0):
			list2+='<li><a href="/problems?group_id='+str(o.id)+'">'+o.title+'</a></li>'

	
	for o in group.objects.filter(type='PRACTICE',active=True):
		if(problems.objects.filter(group=o).count()>0):
			list3+='<li><a href="/problems?group_id='+str(o.id)+'">'+o.title+'</a></li>'

	if request.user.is_authenticated():
		list4+="""    <button class="btn btn-primary dropdown-toggle" type="button" style="width: 100%;text-align:left;" onclick="location.href='/logout';">LOGOUT
  				</button>"""
	else:
		list4+="""    <button class="btn btn-primary dropdown-toggle" type="button" style="width: 100%;text-align:left;" onclick="location.href='/login';">LOGIN
  				</button>"""
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

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
    
def scribble(request):
	return render(request,'scribble.html')