from django.urls import path
from tasks.views import text_view, coder

urlpatterns = [
    path('test', text_view),
    path('coder', coder)
]
