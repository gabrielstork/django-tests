from django.urls import path
from .views import index, discover, comments, new

urlpatterns = [
    path('', index, name='index'),
    path('discover/', discover, name='discover'),
    path('post/<int:id>', comments, name='post'),
    path('new/', new, name='new')
]
