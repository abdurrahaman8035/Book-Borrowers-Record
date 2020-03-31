from django.urls import path
from scanner.views import HomeView, AllStudentsView, new_book, StudentDetailView


app_name = 'scanner'

urlpatterns = [
    path('students/<int:student_id>/', StudentDetailView, name='profile'),
    path('students/<int:student_id>/book', new_book, name='newbook'),
    path('students/', AllStudentsView.as_view(), name='allstudents'),
    path('', HomeView, name='home'),
]
