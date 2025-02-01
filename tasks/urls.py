from django.urls import path
from tasks.views import home, coder, show_specific_task, user_dashboard, manager_dashboard

urlpatterns = [
    path('coder', coder),
    path('specific-task-<int:id>', show_specific_task),
    path('user-dashboard', user_dashboard),
    path('manager-dashboard', manager_dashboard)
]