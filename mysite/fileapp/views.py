from django.template import Context, loader
from polls.models import Poll
from django.http import HttpResponse
from django.core.context_processors import csrf
from fileapp.models import User, File2
from django.shortcuts import redirect
import urllib, cgi, hashlib, sys

def getErrorURL(message, redirect_link):
    return '/error?message='+urllib.quote_plus(message)+'&link='+urllib.quote_plus(redirect_link)

def home(request):
    logged_in_username=''
    try:
        logged_in_username=request.session['username'] #exception may be raised here (for example session does not have key 'username'
        if not logged_in_username: #if i have signed out then session variable will be none
            raise Exception('abcd')
    except Exception:
        return redirect("/signin")

    t = loader.get_template('fileapp/home.html')
    c = Context({
        'username': logged_in_username
    })
    c['files']=[]
    user_=User.objects.get(username=logged_in_username)

    for file in File2.objects.filter(user=user_):
        fileurl=file.thefile.url
        filename=file.filename
        c['files'].append({'filename':cgi.escape(filename,quote=True), 'id':file.id})
    c.update(csrf(request))
    return HttpResponse(t.render(c))



def signin(request):
    t=loader.get_template('fileapp/signin.html')
    c=Context({})
    c.update(csrf(request))
    return HttpResponse(t.render(c))



def register(request):
    t=loader.get_template('fileapp/register.html')
    c=Context({})
    c.update(csrf(request))
    return HttpResponse(t.render(c))    
    


def doregister(request):
    try: # for missing arguements
        u=request.POST['username']
        p=request.POST['password']
        if (not u) or ( not p):
            raise Exception
        try: #see if user exists
            old_user=User.objects.get(username=u)
            return redirect(getErrorURL("User already registered",'/register'))
        except Exception: #user does not already exist; continue processing
            user=User()
            user.username=u
            user.password_hash=hashlib.md5(p+'salt').hexdigest() #save salted hashes for security 
            user.save()
            request.session['username']=u #update current user
    except Exception:
        return redirect(getErrorUrl("Please enter details",'/register'))
    return redirect('/home')



def dosignout(request):
    request.session['username']=None
    return redirect('/signin')



def dosignin(request):
    try: # for missing arguements
        u=request.POST['username']
        p=request.POST['password']
        try: #see if user exists
            user=User.objects.get(username=u)
            try_pass=hashlib.md5(p+'salt').hexdigest()
            if(user.password_hash!=try_pass):
                return redirect()
                raise Exception
            else:
                request.session['username']=u
        except Exception:
            return redirect(getErrorURL("Authentication Failed",'/signin'))
    except Exception:
        return redirect(getErrorURL("Please enter details",'/signin'))
    return redirect('/home')



def error(request):
    try: # for missing arguements
        message=request.GET['message']
        link=request.GET['link']
        t=loader.get_template('fileapp/error.html')
        c=Context({
            'message':message,
            'link':link
        })
        return HttpResponse(t.render(c))
    except Exception:
        return redirect('/home')



def upload(request):
    logged_in_username=''
    try:
        logged_in_username=request.session['username'] 
        if not logged_in_username:
            raise Exception('abcd')
    except Exception:
        return redirect("/signin")

    newfile = File2()
    try:
        newfile.filename=request.FILES['file'].name
        newfile.user=User.objects.get(username=logged_in_username)
        newfile.thefile=request.FILES['file']
    except Exception:
        return redirect(getErrorURL("No file uploaded","/home"))
    
    newfile.save()
    return redirect("/home")

def textEscape(text):
    return text

def download(request):
    logged_in_username=''
    try:
        logged_in_username=request.session['username'] 
        if not logged_in_username: 
            raise Exception('abcd')
    except Exception:
        return redirect("/home")
    
    user=User.objects.get(username=logged_in_username)
    file=File2.objects.get(id=request.GET['id'])
    if(file.user!=user):
        return redirect(getErrorURL("You do not have permissions to download this content", "/home"))
    
    filename = file.filename
    response = HttpResponse(file.thefile.file, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="%s"' % (filename)
    return response
        
    
# def perr(x):
#     errfile=open("errfile","a")
#     errfile.write(str(x))
#     errfile.close()
