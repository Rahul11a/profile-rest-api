from django.urls import path
# This is the model we created and is in our local directory
from profiles_api import views


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),# as_view() is call
]
