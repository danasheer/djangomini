from django.shortcuts import render
from employee.models import Employee


# Create your views here.
def showployees(request):

    context = {
        "employees" : Employee.objects.all()
    }
        
    return render(request, 'employees.html', context)


def showprinters(request):
    return render(request, 'printers.html')
