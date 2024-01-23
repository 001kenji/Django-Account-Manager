from django.shortcuts import render,HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from .models import Teachers


# Create your views here.
def LoginUser(request):
    userpage = loader.get_template('index.html')
    
    return HttpResponse(userpage.render())

def loggedUser(request):
    teacherData = Teachers.objects.all().values()
    loggedUser = loader.get_template('teacherTemp.html')
    userpage = loader.get_template('index.html')
  
    if request.method=='POST':
        logname = request.POST['logname']
        logpassword = request.POST['logpassword']
        
        content = {
                    'name' : 'null',
                    'logpassword' : 'null'
                }
        for x in teacherData :
            if x['username'] == logname and x['password'] == logpassword:
                  content = {'name' : logname}
                #   x['online'] = True
                #   values = Teachers.objects.all().values()
                  Teachers.objects.filter(username=logname).update(online=True)

                  return HttpResponse(loggedUser.render(content,request))
                  print(teacherData)
        return HttpResponse(userpage.render(content,request))
        
def loggingOut(request):
    teacherData = Teachers.objects.all().values()
    loggedUser = loader.get_template('teacherTemp.html')
    userpage = loader.get_template('index.html')
   

    logname = request.POST['name']
    
    content = {
                'name' : 'null',
                'logpassword' : 'null'
            }
    for x in teacherData :
        if x['username'] == logname:
                
                # x['online'] = False
                Teachers.objects.filter(username=logname).update(online=False)

                
                return HttpResponse(userpage.render(content,request))
                print(teacherData)
    return HttpResponse(userpage.render(content,request))
         