from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import student
from .forms import stdreg

# Create your views here.
def index(request):
    if request.method == 'POST':
        fm = stdreg(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = student(name=nm,email=em,password=pw)
            reg.save()
            return HttpResponseRedirect('/')
    else:
        fm=stdreg()
        det = student.objects.all()
    return render(request,'index.html',{'form':fm,'det':det})

def delete_data(request,id):
    if request.method == 'POST':
        pi = student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update(request,id):
    if request.method == 'POST':
        pi = student.objects.get(pk=id)
        fm = stdreg(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = student.objects.get(pk=id)
        fm = stdreg(instance=pi)
    return render(request,'update.html',{'form':fm})