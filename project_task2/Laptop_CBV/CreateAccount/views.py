from django.shortcuts import render,redirect

# Create your views here.
from django.views import View
from django.contrib import messages
from django.contrib.auth import  authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm


class RegisterView(View):
    def get(self,request):
        form = UserCreationForm()
        template_name = 'CreateAccount/register.html'
        context = {'form': form}
        return render(request, template_name, context)
    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        template_name = 'CreateAccount/register.html'
        context = {'form': form}
        return render(request, template_name, context)

class loginView(View):
    def get(self,request):
        template_name = 'CreateAccount/login.html'
        context = {}
        return render(request, template_name, context)
    def post(self,request):
        username = request.POST.get("uname")
        password = request.POST.get("pw")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('show_laptop')
        else:
            messages.error(request,"invalid username or password")
        template_name = 'CreateAccount/login.html'
        context = {}
        return render(request, template_name, context)


class logoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login')
