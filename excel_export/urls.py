from django.urls import path

from .views import export_to_xls

urlpatterns = [
    path('export', export_to_xls),
]