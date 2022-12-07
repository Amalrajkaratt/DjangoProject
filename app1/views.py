from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import Table1,Gallery
from . forms import RegisterForm,LoginForm,UpdateForm,ChangePassword
from django.contrib import messages
from django.contrib.auth import logout as logouts
from assignment1 import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request,'index.html')


def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            email=form.cleaned_data['Email']
            photo=form.cleaned_data['Photo']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['ConfirmPassword']

            user=Table1.objects.filter(Email=email).exists()

            if user:
                messages.warning(request,"Email exists")
                return redirect('/register')
            elif password!=confirmpassword:
                messages.warning(request,"Password Mismatch")
                return redirect('/register')
            else:
                tab=Table1(Name=name,Age=age,Place=place,Email=email,Photo=photo,Password=password)
                tab.save()
                messages.warning(request,"Sign up Success")
                return redirect('/')
    else:
        form=RegisterForm()
    return render(request, 'register.html',{'form':form})

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']

            user=Table1.objects.get(Email=email)

            if not user:
                messages.warning(request,"Email does not exist")
                return redirect('/login')
                
            elif password!=user.Password:
                messages.warning(request,"Password incorrect")
                return redirect('/login')

            else:
                messages.warning(request,"Login success")
                return redirect('/home/%s'%user.id)
                
    else:
        form=LoginForm()
    return render(request, 'login.html',{'form':form})

def home(request,id):
    user=Table1.objects.get(id=id)
    return render(request,'home.html',{'user':user})
    
def update(request,id):
    user=Table1.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
            messages.warning(request,"Success")
            return redirect('/home/%s'%user.id)
    else:
      form=UpdateForm(instance=user)
    return render(request,'update.html',{'form':form,'user':user})

def changepassword(request,id):
    user=Table1.objects.get(id=id)
    if request.method=='POST':
        form=ChangePassword(request.POST)
        if form.is_valid():
            oldpassword=form.cleaned_data['OldPassword']
            newpassword=form.cleaned_data['NewPassword']
            confirmnewpassword=form.cleaned_data['ConfirmNewPassword']

            if user.Password!=oldpassword:
                messages.warning(request,"Incorrect Password")
                return redirect('/changepassword/%s'%user.id)
            elif oldpassword==newpassword:
                messages.warning(request,"Password not available")
                return redirect('/changepassword/%s'%user.id)
            elif newpassword!=confirmnewpassword:
                messages.warning(request,"Password Mismatch")
                return redirect('/changepassword/%s'%user.id)
            else:
                user.Password=newpassword
                user.save()
                messages.warning(request,"Success")
                return redirect('/')
    else:
        form=ChangePassword()
    return render(request,'changepassword.html',{'form':form,'user':user})


def logout(request):
    logouts(request)
    messages.warning(request,"Logout success")
    return redirect('/')

# def gallery(request):
#     if request.method=='POST':
#         form=GalleryForm(request.POST)
#         if form.is_valid():
#             name=form.cleaned_data['Name']
#             age=form.cleaned_data['Age']
#             place=form.cleaned_data['Place']
#             email=form.cleaned_data['Email']
#             photo=form.cleaned_data['Photo']
#             password=form.cleaned_data['Password']
#             confirmpassword=form.cleaned_data['ConfirmPassword']

#             user=Gallery.objects.filter(Email=email).exists()

#             if user:
#                 messages.warning(request,"Email exists")
#                 return redirect('/gallery')
#             elif password!=confirmpassword:
#                 messages.warning(request,"Password Mismatch")
#                 return redirect('/gallery')
#             else:
#                 tab=Table1(Name=name,Age=age,Place=place,Email=email,Photo=photo,Password=password)
#                 tab.save()
#                 messages.warning(request,"Success")
#                 return redirect('/')
#     else:
#         form=GalleryForm()
#     return render(request, 'gallery.html',{'form':form})

def gallery(request):
    users=Gallery.objects.all()
    return render(request,'gallery.html',{'users':users})


def details(request,id):
    user=Gallery.objects.get(id=id)
    return render(request,'details.html',{'user':user})

def mail(request):
    if request.method=='POST':
        cname=request.POST.get('contact_name')
        cemail=request.POST.get('contact_email')
        cmessage=request.POST.get('contact_message')
        toemail='amalraj0310@gmail.com'
        res = send_mail(cname,cmessage,settings.EMAIL_HOST_USER,[toemail],fail_silently=False)
        if(res==1):
            msg="Mail sent successfully"
        else:
            msg="Message could not sent"
        return HttpResponse(msg)
    else:
        return render(request,'index.html')

def home2(request):
    user=Table1.objects.all()
    return render(request,'home2.html',{'user':user})        