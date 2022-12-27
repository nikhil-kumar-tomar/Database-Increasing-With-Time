from django.shortcuts import render,HttpResponseRedirect
from .models import *
from .forms import *
# Create your views here.
def see_all(request):
    stu_class=studs.objects.all()
    context={
        'stu_class':stu_class,
    }
    return render(request,"students/all databases.html",context)

def student(request,roll):
    student_info=studs.objects.get(roll=roll)
    context={
        'student':student_info,
    }
    return render(request,"students/student.html",context)

def search(request):
    if request.method == 'POST':
        form = roll_s(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(f"/students/{request.POST['roll']}")
    else:
        form = roll_s()
    return render(request, 'students/get_info.html', {'form':form})

def index(request):
    if request.method=="POST":
        form =indexes(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(f"{request.POST['choice']}/")
    else:
        form=indexes()
    context={
        'form':form,
    }
    return render(request,"students/index.html",context)

def ent_info(request):
    if request.method == 'POST':
        form = ent_infos(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f"/students/{request.POST['roll']}/")
    else:
        form=ent_infos

    context={
        'form':form,
    }
    return render(request,"students/ent_info.html",context)

def completed(request):
    return render(request,"students/completed.html")

# Have to create update one
def update(request):
    if request.method == 'POST':
        form = roll_s(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(f"/students/update/{request.POST['roll']}")
    else:
        form = roll_s()
    return render(request, 'students/get_info.html', {'form':form})


def update_roll(request,roll_no):
    student_info=studs.objects.get(roll=roll_no)
    if request.method=="POST":
        form=ent_infos(request.POST,instance=student_info)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f"/students/{request.POST['roll']}/")
    else:
        form=ent_infos(instance=student_info)
    return render(request,"students/update_info.html",{"form":form})
    