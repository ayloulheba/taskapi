from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecordViewSet.as_view(), name='api_record_list'),
    # Add other URL patterns for other views if needed
]