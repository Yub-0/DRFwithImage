from django.urls import path

from api import views

urlpatterns = [
    path('uploadImg', views.UploadProduct.as_view()),
    path('image', views.ViewProducts.as_view())
]