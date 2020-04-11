from django.urls import path
from scanner.views import (HomeView,
                           AllStudentsView,
                           new_book,
                           StudentDetailView,
                           StudentDelete,
                           RenewBookView,
                           Search_result,
                           Register_student,
                           StudentEditProfile)


app_name = 'scanner'

urlpatterns = [
    path('', HomeView, name='home'),
    path('register/', Register_student.as_view(), name='register_student'),
    path('search/', Search_result.as_view(), name='search'),
    path('students/', AllStudentsView.as_view(), name='allstudents'),
    path('students/<int:student_id>/', StudentDetailView, name='profile'),
    path('book/<int:student_id>/', new_book, name='book-new'),
    path('students/<int:student_id>/<int:pk>/delete', StudentDelete.as_view(), name='deletebook'),
    path('students/<int:student_id>/<int:pk>/renew', RenewBookView.as_view(), name='renew-book'),
    path('students/<int:pk>/edit', StudentEditProfile.as_view(), name='edit_student_profile'),
]
