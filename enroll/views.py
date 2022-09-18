from django.shortcuts import render, redirect
from .forms import studentregisteration
from .models import User


# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = studentregisteration(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = studentregisteration()
        
    stud = User.objects.all()

    context={
        'form': fm,
        'student': stud
    }
    return render(request, 'enroll/addandshow.html', context)

def deletee(request, id):
    if request.method == 'POST':
        stud = User.objects.get(pk=id)
        stud.delete()
    return redirect('add_show')

def update(request, id):
    if request.method == 'POST':
        stud = User.objects.get(pk=id)
        print(stud)
        fm = studentregisteration(request.POST, stud)
        print(fm)
        if fm.is_valid():
            fm.save()
    return render(request, 'enroll/updatestudent.html', {'form': fm})