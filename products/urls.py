from django.urls import path
from .views import index, update, delete

urlpatterns =[
    path('home', index, name='home'),
    path('update/<int:todo_id>/', update, name='update'),
    path('detele/<int:todo_id>/', delete, name='delete'),
]