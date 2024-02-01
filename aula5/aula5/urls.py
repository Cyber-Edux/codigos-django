from django.urls import path
from blog import views

urlpatterns = [
    path('feed', views.feed),
    path('publicate', views.publicate)
]
