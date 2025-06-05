
from django.urls import path
from . import views
urlpatterns = [
    path('', views.booklist, name='BooksList'),
    path('addbook', views.addbook, name='addbook'),
    path('updatebook/<int:id>', views.updatebook, name='updatebook'),
    path('deletebook/<int:id>', views.deletebook, name='deletebook'),
]