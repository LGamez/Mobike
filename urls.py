from django.urls import path
import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
