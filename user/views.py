from django.shortcuts import render ,redirect ,HttpResponse
from .forms import MyForm
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    form = MyForm()
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password1']  
        email = request.POST['email']
        user = User.objects.create(
            username=username,
            email=email
        )  
        user.set_password(password)
        user.save()
    # if request.method == 'POST':
    #     form = MyForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponse("success")

    context = {
        'form':form
    }
    return render(request,'register.html',context)