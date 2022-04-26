from django.urls import path

from api import views

urlpatterns = [
    path('uploadImg', views.UploadImage.as_view()),
    path('image', views.ViewImage.as_view())
]