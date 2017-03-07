from django.shortcuts import render
from django.contrib.auth.views import login,logout
from django.http import HttpResponseRedirect, HttpResponse
from problems.models import group,problems
# Create your views here.
def home(request):
	list=""
	list+='<li><a href="/home">Home</a>'
	list+='<li>CONTEST</li>'
	for o in group.objects.filter(type='CONTEST'):
		if(problems.objects.filter(group=o).count()>0):
			list+='<li><a href="/problems?group_id='+str(o.id)+'">'+o.title+'</a></li>'
	list+='<li>LAB</li>'
	for o in group.objects.filter(type='LAB'):
		if(problems.objects.filter(group=o).count()>0):
			list+='<li><a href="/problems?group_id='+str(o.id)+'">'+o.title+'</a></li>'

	list+='<li>PRACTICE</li>'
	for o in group.objects.filter(type='PRACTICE'):
		if(problems.objects.filter(group=o).count()>0):
			list+='<li><a href="/problems?group_id='+str(o.id)+'">'+o.title+'</a></li>'
	if request.user.is_authenticated():
		list+='<li><a href="/logout">Logout</a>'
	else:
		list+='<li><a href="/login">Login</a>'
	return render(request,'main.html',{'list':list})

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