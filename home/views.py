# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Contact
from blog.models import Post
from django.core.paginator import Paginator
from datetime import datetime

#from math import ceil
# import the logging library
#import logging

# Get an instance of a logger
#logger = logging.getLogger(__name__)
# Create your views here.

# Create your views here.
def home(request):
    allPosts=Post.objects.all()

    paginator=Paginator(allPosts,2)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1

    try:
        allPosts=paginator.page(page)
    except(EmptyPage,InvalidPage):
        allPosts=paginator=paginator.page(paginator.num_pages)
    content={'allPosts':allPosts}
    return render(request,'home/index.html',content)
    #return HttpResponse('This is Home')


def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        
    #    print(name,email,phone,desc)
        if len(name) < 2 or len(email) < 2 or len(phone) < 2 or len(desc) < 2:
            messages.error(request,"error")
        else:
            contact = Contact(name=name, email=email, phone=phone, desc=desc,timestamp=datetime.today())
            contact.save()
            messages.success(request,"correct")
    return render(request, 'home/contact.html')

    
#    return render(request,'home/contact.html',)

 #   return HttpResponse('This is home contact')

def about(request):
    return render(request,'home/about.html')
#    return HttpResponse('This is home about')


def search(request):
    query=request.GET['query']
    if len(query)>100:
        # allPosts=[]
        allPosts=Post.objects.none()
    else:
        allPoststitle=Post.objects.filter(title__icontains=query)
        allPostscontent=Post.objects.filter(content__icontains=query)
        allPostsslug=Post.objects.filter(slug__icontains=query)

        allPosts=allPoststitle.union(allPostscontent,allPostsslug)
    if allPosts.count() == 0:
        messages.error(request,"No search results found plear search with another query")
       
    # allPosts:Post.objects.all()
    params={'allPosts':allPosts,'query':query}
    return render(request,'home/search.html',params)

    # return HttpResponse('search')



def handlesignup(request):
    if request.method =='POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']


        if len(username)>10:
            messages.error(request,'Your username must be under 10')
            return redirect('home')
        if pass1 != pass2:
            messages.error(request,'Your Password Donot Match')
            return redirect('home')
        if not username.isalnum():
            messages.error(request,'Your username must be alpha numeric')
            return redirect('home')
        
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,'Your Account has been successfully created')      
        return redirect('home')

    else:
        return HttpResponse('<b>404 - not found</b>')

def handlelogin(request):
    if request.method =='POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']   

        user = authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            messages.success(request,'Successfully logged in')
            return redirect('home')
        else:
            messages.error(request,'please try again later')
            return redirect('home')

    # return HttpResponse()
    return HttpResponse('<b>404 - not found</b>')

def handlelogout(request):
    logout(request)
    messages.success(request,'successfully logged out')
    return redirect('home')

    # return HttpResponse()