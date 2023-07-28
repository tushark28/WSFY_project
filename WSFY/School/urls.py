from django.urls import path
from . import views

app_name = 'School'

urlpatterns = [
    path('input_marks/', views.input_marks, name='input_marks'),
    path('view_marks/', views.view_marks, name='view_marks'),
]