from django.urls import path
from tasks.views import coder, show_specific_task, user_dashboard, manager_dashboard,test_file, common_dashboard

urlpatterns = [
    path('coder', coder),
    path('specific-task-<int:id>', show_specific_task),
    path('user-dashboard', user_dashboard),
    path('manager-dashboard', manager_dashboard),
    path('test-file', test_file),
    path('common-dashboard', common_dashboard)
]