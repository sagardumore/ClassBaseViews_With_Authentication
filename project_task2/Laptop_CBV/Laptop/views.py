from django.shortcuts import render,redirect

# Create your views here.
from django.views import View
from .forms import LaptopModelForm
from .models import Laptop
from django.contrib.auth.mixins import LoginRequiredMixin

class AddLaptopView(LoginRequiredMixin,View):
    def get(self,request):
        form=LaptopModelForm()
        context={'form':form}
        template_name='Laptop/addlaptopform.html'
        return render(request,template_name,context)
    def post(self,request):
        form = LaptopModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_laptop')
        context = {'form': form}
        template_name = 'Laptop/addlaptopform.html'
        return render(request, template_name, context)

class ShowLaptopView(LoginRequiredMixin,View):
    def get(self,request):
        laptop_obj=Laptop.objects.all()
        template_name= 'Laptop/showlaptopinfo.html'
        context={'laptop_obj':laptop_obj}
        return render(request,template_name,context)


class deleteLaptopView(View):
    def get(self,request,i):
        laptop=Laptop.objects.get(id=i)
        template_name = 'Laptop/deletelaptop.html'
        context = {'laptop': laptop}
        return render(request, template_name, context)

    def post(self,request,i):
        laptop=Laptop.objects.get(id=i)
        laptop.delete()
        return redirect('show_laptop')

class updateLaptopView(View):
    def get(self,request,i):
        laptop=Laptop.objects.get(id=i)
        form = LaptopModelForm(instance=laptop)
        template_name = 'Laptop/addlaptopform.html'
        context = {'form': form}
        return render(request, template_name, context)
    def post(self,request,i):
        laptop=Laptop.objects.get(id=i)
        form =LaptopModelForm(request.POST,instance=laptop)
        if form.is_valid():
            form.save()
            return redirect('show_laptop')


