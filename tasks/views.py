from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm
from tasks.models import Employee, Task

# Create your views here.
def home(request):
    return HttpResponse('<h1 style="color:green">Wellcome to the Home page!</h1>')

def coder(request):
    return HttpResponse('<marquee style="font-weight:bold; font-size:60px;">I am a passioneted programmer from bangladesh and now i am able to work world wide</marquee>')

def show_specific_task(request, id):
    print("id: ", id)
    print("id type: ", type(id))
    return HttpResponse(f"This is specific task page! task id is {id}")


def user_dashboard(request):
    return render(request, 'dashboard/user-dashboard.html')

def manager_dashboard(request):
    return render(request, 'dashboard/manager-dashboard.html')

def common_dashboard(request):
    return render(request, 'dashboard/common-dashboard.html')

def test_file(request):
    context = {
        'names': ['Mahmud', 'Ahamed', 'Hasan ali', 'Ali abdal'],
        'age': 23
    }
    return render(request, 'test.html', context)


def create_task(request):
    employees = Employee.objects.all()
    form = TaskForm(employees = employees)


    if request.method == 'POST':
        form = TaskForm(request.POST, employees = employees)
        if form.is_valid():
            data = form.cleaned_data
            title = data.get('title')
            description = data.get('description')
            due_date = data.get('due_date')
            assigned_to = data.get('assigned_to')

            task = Task.objects.create(title=title, description=description, due_date=due_date)
            for emp_id in assigned_to:
                employee = Employee.objects.get(id=emp_id)
                task.assigned_to.add(employee)
            
            return HttpResponse(f'Task: {title} added successfully!')

    # form = TaskForm(employees = employees)
    context = {'form':form}
    return render(request, 'create_task.html', context)