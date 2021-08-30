
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name="homepage"),
    path('create',views.create,name="createpage"),
    path('update/<int:id>',views.update,name="updatepage"),
    path('delete/<int:id>',views.delete,name="deletepost")
]
 