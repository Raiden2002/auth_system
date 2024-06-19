from django.shortcuts import render ,redirect ,HttpResponse
from .forms import MyForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def register(request):
    form = MyForm()
    # if request.method =='POST':
    #     username = request.POST['username']
    #     password = request.POST['password1']  
    #     email = request.POST['email']
    #     user = User.objects.create(
    #         username=username,
    #         email=email
    #     )  
    #     user.set_password(password)
    #     user.save()
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("success")

    context = {
        'form':form
    }
    return render(request,'register.html',context)
def log_in(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try :
            user = User.objects.get(username=username)
            # print('user found',user)
        except Exception as e:
            print(e)    
        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            print('successfull')
            return redirect('home')
        else:
            return HttpResponse("check ur input")    
    return render(request,'login.html')
def log_out(request):
    logout(request)
    return redirect('login')