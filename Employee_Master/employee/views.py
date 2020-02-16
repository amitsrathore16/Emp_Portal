from django.shortcuts import render, redirect
from .forms import AddEmpForm
from .models import Employee

# Create your views here.
def home(request):
    all_item = Employee.objects.all()
    return render(request, 'home.html', {'all':len(all_item)})


def add(request):
    if request.method == 'POST':
        form = AddEmpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('add')
    else:
        form = AddEmpForm()
        return render(request, 'add.html', {'form': form})


def view(request):
    emp = Employee.objects.all()
    email = Employee.objects.values('email')
    print(list(email))
    return render(request, 'view.html', {'emp': emp})
