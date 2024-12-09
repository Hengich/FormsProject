from django.urls import path
from .views import FormAPIView

urlpatterns = [
    path('get_form/', FormAPIView.as_view(), name='get_form'),
]
