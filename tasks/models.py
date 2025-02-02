from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    # task_set : hidden column 
    # tasks : changed by related_name in child

class Task(models.Model):
    project = models.ForeignKey('Project', 
            on_delete=models.CASCADE,
            default=1,
            related_name='tasks'
    )
    assigned_to = models.ManyToManyField(Employee, related_name='tasks')
    title = models.CharField(max_length=250)
    description = models.CharField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default= False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # taskdetail: a default hidden column for reverse relations
    # details: chnaged by related name in the child


class TaskDetail(models.Model):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'
    PRIORITY_OPTIONS = (
        (HIGH, 'HIGH'),
        (MEDIUM, 'MEDIUM'),
        (LOW, 'LOW'),
    )
    task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name='details')
    assigned_to = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=PRIORITY_OPTIONS, default=LOW)

    # ORM = Object relational mapper -> django to sql query 
    # Task.objects.get(id = 2) -> select * from task where id = 2

class Project(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField()

    # task_set : hidden column
    # tasks : changed by related name in the child
