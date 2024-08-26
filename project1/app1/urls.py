from django.urls import path
from .views import home, index, task_list, task_detail, task_create, task_update, task_delete


urlpatterns = [
    path('', task_list, name='task'),
    path('detail/<int:id>/', task_detail, name='detail'),
    path('update/<int:id>/', task_update, name='update'),
    path('delete/<int:id>/', task_delete, name='delete'),
    path('create/',task_create, name='create'),
    
    path('home/', home),
    path('index/', index, name='index'),  # Added new URL path
    
]
