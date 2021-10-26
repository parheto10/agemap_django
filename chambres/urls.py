from django.urls import path
from .views import chambres

urlpatterns = [
    path('', chambres, name="chambres"),
]