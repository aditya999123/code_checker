from django.shortcuts import render
from django.contrib.auth.views import login,logout
from django.http import HttpResponseRedirect, HttpResponse
from problems.models import group,problems
# Create your views here.
def home(request):
	list1=""
	list2=""
	list3=""
	list4=""
	for o in group.objects.filter(type='CONTEST'):
		if(problems.objects.filter(group=o).count()>0):
			list1+='<li><a href="/problems?group_id='+str(o.id)+'">'+o.title+'</a></li>'
	
	for o in group.objects.filter(type='LAB'):
		if(problems.objects.filter(group=o).count()>0):
			list2+='<li><a href="/problems?group_id='+str(o.id)+'">'+o.title+'</a></li>'

	
	for o in group.objects.filter(type='PRACTICE'):
		if(problems.objects.filter(group=o).count()>0):
			list3+='<li><a href="/problems?group_id='+str(o.id)+'">'+o.title+'</a></li>'
	if request.user.is_authenticated():
		list4+='<a style="color: white;" href="/logout">LOGOUT</a>'
	else:
		list4+='<a style="color: white;" href="/login">LOGIN</a>'
	return render(request,'main.html',{'list1':list1,'list2':list2,'list3':list3,'list4':list4})

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