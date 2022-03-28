from .models import *
from django.shortcuts import render,redirect
from .form import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



# Create your views here.
def indexview(request):
    return render(request,'home.html')

def booklistview(request):
    all_book = BookModel.objects.all()
    context={'all_book':all_book}
    return render(request,'book.html',context)

def userlistview(request):
    all_user=User.objects.filter(is_superuser=False)
    return render(request,'user.html',{'all_user':all_user})

def adduserview(request):
    form=SignupForm()
    if request.method == 'POST':
        form=SignupForm(request.POST,request.FILES)
        if form.is_valid():
            form=SignupForm(request.POST,request.FILES)
            form.save()
            messages.success(request,'User Added Successfully!')
            return redirect('/adduser/')
    else:
        form=SignupForm()
    return render(request,'add_user.html',{'form':form})

def IssueBookView(request,id):
    get_book=BookModel.objects.get(id=id)
    all_user=User.objects.filter(is_superuser=False)
    if request.method == 'POST':
        book=get_book
        user=request.POST['user']
        IssueBook(
            book=book,
            user=User.objects.get(username=user),
        ).save()
        return redirect('/book/')
    return render(request,'issue_book.html',{'all_user':all_user})

def IssueBooKDetailView(request):
    issued_books=IssueBook.objects.filter(user=request.user)
    return render(request,'detail.html',{'issued_books':issued_books})

def SigninView(request):
    form = SigninForm()
    if request.method == 'POST':
        uname = request.POST['username']
        upass = request.POST['password']
        user = authenticate(username=uname, password=upass)
        if user is None:
            messages.error(request, 'Please Enter Correct Credinatial')
            return redirect('/')
        else:
            login(request, user)
            if(user.is_superuser):
                return redirect('/home/')
            else:
                return redirect('/issuebook/')
    else:
        if request.user.is_authenticated:
            return redirect('/home/')
        else:
            return render(request, 'login.html', {'form': form})

def logoutview(request):
    logout(request)
    return redirect('/')