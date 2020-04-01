from django.urls import path
from scanner.views import HomeView, AllStudentsView, new_book, StudentDetailView, StudentDelete


app_name = 'scanner'

urlpatterns = [
    path('', HomeView, name='home'),
    path('students/', AllStudentsView.as_view(), name='allstudents'),
    path('students/<int:student_id>/', StudentDetailView, name='profile'),
    path('book/<int:student_id>/', new_book, name='book-new'),
    path('students/<int:student_id>/<int:pk>/delete', StudentDelete.as_view(), name='deletebook'),
]
