from django.urls import path
from django.views.generic import TemplateView
from .views import HomeView, Success, BookView, BookListView

urlpatterns = [
    path('', HomeView.as_view(), name = 'homePage'),
    path('students_list/', Success.as_view(), name = 'students_list'),
    path('BookAdd/', BookView.as_view(), name = 'BookAdd'),
    path('BookList/', BookListView.as_view(), name = 'BookList'),
]