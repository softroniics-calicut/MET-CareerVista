from django.shortcuts import render,redirect
from django.http import HttpResponse
from  django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import userreg,companyreg,job,application,notification
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate,login as auth_login
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def userindex(request):
    return render(request,'userindex.html')

def companyindex(request):
    return render(request,'companyindex.html')







def userregistration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        file = request.FILES['file']
        username = request.POST.get('username')
        password = request.POST.get('password')

        if userreg.objects.filter(email=email).exists():
            return render(request,'registrationuser.html',{'message':'Email already exists'})
        if userreg.objects.filter(contact=contact).exists():
            return render(request,'registrationuser.html',{'message':'Contact already exists'})
        if companyreg.objects.filter(username=username).exists():
            return render(request,'registrationuser.html',{'message':'Username already taken'})
        
        data = userreg(name=name,email=email,contact=contact,file=file,username=username,password=password)
        data.save()
        return redirect(logins)
    
    else:
        return render(request,'registrationuser.html')



def companyregistration(request):
    if request.method == 'POST':
        companyname = request.POST.get('companyname')
        address = request.POST.get('address')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if companyreg.objects.filter(email=email).exists():
            return render(request,'registrationcompany.html',{'message':'Email already exists'})
        if companyreg.objects.filter(contact=contact).exists():
            return render(request,'registrationcompany.html',{'message':'Contact already exists'})
        if companyreg.objects.filter(username=username).exists():
            return render(request,'registrationcompany.html',{'message':'Username already taken'})

        data = companyreg(companyname=companyname,address=address,email=email,contact=contact,username=username,password=password)
        data.save()
        return redirect(logins)
    else:
        return render(request, 'registrationcompany.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logins(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        context={'message':'Invalid User Credentials'}

        admin_user = authenticate(request,username=username,password=password)
        if admin_user is not None and admin_user.is_staff:
            auth_login(request,admin_user)
            return redirect('admin:index')
        
        if userreg.objects.filter(username=username,password=password).exists():
            userdetail=userreg.objects.get(username=request.POST['username'], password=password)
            if userdetail.password == request.POST['password'] and userdetail.status=='accepted':
                request.session['uid'] = userdetail.id
            

                return redirect(userindex)
            else:
                return render(request,'login.html',{'message':'wait for admin approval'})
            
        elif companyreg.objects.filter(username=username,password=password).exists():
            userdetail=companyreg.objects.get(username=request.POST['username'], password=password)
            if userdetail.password == request.POST['password'] and userdetail.status=='accepted':
                request.session['cid'] = userdetail.id


                return redirect(companyindex)
            else:
                return render(request,'login.html',{'message':'wait for admin approval'})
            
        else:
            return render(request, 'login.html',{'message': 'Invalid Username or Password'})
    else:
        return render(request,'login.html')
    


def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
      del request.session[key]
    return redirect(index)







# user..................................................
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def userprofile(request):
    if 'uid' in request.session:
        tem=request.session['uid']
        vpro=userreg.objects.get(id=tem)
        return render(request,'userprofile.html',{'result':vpro})
    else:
        return redirect(logins)


def userprofileedit(request):
    return render(request,'userprofileedit.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def updat(request,id):
    if 'uid' in request.session:
        upt=userreg.objects.get(id=id)
        return render(request,'userprofileedit.html',{'result':upt})
    else:
        return redirect(logins)

def updates(request,id):
    user = userreg.objects.get(id=id)
    if request.method=="POST":
        user.name=request.POST.get('name')
        user.contact=request.POST.get('contact')
        user.email=request.POST.get('email') 
        if 'file' in request.FILES:
            user.file = request.FILES('file')
        user.username = request.POST.get('username')
        user.password=request.POST.get('password')
        user.save()
        return redirect(userprofile)
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def jobview(request):
    if 'uid' in request.session:
        if request.method == "GET":
            data = job.objects.all().order_by('-id')
            return render(request,'viewjob.html',{'data':data})
    else:
        return redirect(logins)
    

def search(request):
  if request.method == 'POST':
    search = request.POST.get('search')
    data = job.objects.filter(job_name=search)
    return render(request,'viewjob.html',{'data':data})
  
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def applications(request):
    id=request.session['uid']
    if request.method=="POST":
        jobid = request.POST.get('jobid')
        user =userreg.objects.get(id=id)
        jobs = job.objects.get(id=jobid)
        if application.objects.filter(user_id=user,job_id=jobid).exists():
            return render(request,'viewjob.html',{'message':'Already applied'})

        context = {
            'data1':"Applied successfully"
        }
        user =userreg.objects.get(id=id)
        jobs = job.objects.get(id=jobid)
       
        # company = companyreg.objects.get(id=job.company_id.id)

        data1 = application.objects.create(user_id=user,job_id=jobs.id)
        data1.save()     
    return render(request,'viewjob.html',context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def appliedjobs(request):
    if 'uid' in request.session:
        id=request.session['uid']
        user = userreg.objects.get(id=id)
        data = application.objects.filter(user_id=user).order_by('-id')
        return render(request,'appliedjobs.html',{'data':data})
    else:
        return redirect(logins)



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def notifications(request):
    if 'uid' in request.session:
        notificationss = notification.objects.all().order_by('-id')
        return render(request,'notificationuser.html',{'data':notificationss})
    else:
        return redirect(logins)



# company......................................
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def companyprofile(request):
    if 'cid' in request.session:
        tem=request.session['cid']
        vpro=companyreg.objects.get(id=tem)
        return render(request,'companyprofile.html',{'result':vpro})
    else:
        return redirect(logins)


def companyprofileedit(request):
    return render(request,'companyprofileedit.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def companyupdat(request,id):
    if 'cid' in request.session:
        upt=companyreg.objects.get(id=id)
        return render(request,'companyprofileedit.html',{'result':upt})
    else:
        return redirect(logins)

def companyupdates(request,id):
    if request.method=="POST":
        companyname=request.POST.get('companyname')
        address = request.POST.get('address')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        username = request.POST.get('username')
        password=request.POST.get('password')
        registration=companyreg(companyname=companyname,address=address,contact=contact,email=email,username=username,password=password,id=id)
        registration.save()
        return redirect(companyprofile)
    

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def addjob(request):
    if 'cid' in request.session:
        if request.method=="POST":
            tem=request.session['cid']
            job_name = request.POST.get('jobname')
            job_description = request.POST.get('description')
            context = {
                'data':"Added successfully"
            }

            data1 = companyreg.objects.get(id=tem)
            if data1:
                data = job.objects.create(company_id=data1,job_name=job_name,job_description=job_description)
                data.save()
                return render(request,'addjobcompany.html',context)
            else:
                return HttpResponse("error")
        else:
            return render(request,'addjobcompany.html')
    else:
        return redirect(logins)
    

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def managejob(request):
    if 'cid' in request.session:
        tem=request.session['cid']
        vpro=job.objects.filter(company_id=tem).order_by('-id')
        return render(request,'managejob.html',{'result':vpro})
    else:
        return redirect(logins)


def editjob(request,id):
    tem=request.session['cid']
    data1 = companyreg.objects.get(id=tem)
    jobs =job.objects.get(company_id=data1,id=id)
    if request.method == "POST":
        jobs.job_name = request.POST.get('jobname')
        jobs.job_description = request.POST.get('description')
        jobs.save()
        return redirect(managejob)
    else:
        return render(request,'managejobedit.html',{'result':jobs})
    
def deletejob(request, id):
    company_id = request.session.get('cid')
    if company_id:
        company = companyreg.objects.get(id=company_id)
        job_of_company = job.objects.get(company_id=company, id=id)
        job_of_company.delete()
        return redirect(managejob)


@cache_control(no_cache=True, must_revalidate=True, no_store=True) 
def viewapplication(request):
    if 'cid' in request.session:
        company_id = request.session.get('cid')
        applications = None
        if company_id:
            company = companyreg.objects.get(id=company_id)
            jobs_of_company = job.objects.filter(company_id=company)
            applications = application.objects.filter(job__in=jobs_of_company).order_by('-id')

        return render(request, 'viewapplication.html', {'data': applications})
    else:
        return redirect(logins)


def applicationaccept(request, id):
    if request.method == 'POST':
        applications = application.objects.get(id=id)
        action = request.POST.get('action') 
        if action == 'Accept':
            applications.status = 'Accepted'
        elif action == 'Reject':
            applications.status = 'Rejected'
        applications.save()
        return redirect(viewapplication)
    return redirect(viewapplication) 
    

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def notificationcom(request):
    if 'cid' in request.session:
        notificationss = notification.objects.all().order_by('-id')
        return render(request,'notificationcompany.html',{'data':notificationss})
    else:
        return redirect(logins)