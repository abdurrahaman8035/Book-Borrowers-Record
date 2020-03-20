from django.urls import path
from django.views.generic import TemplateView
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    # path('students_list/', Success.as_view(), name = 'students_list'),
    # path('BookAdd/', BookView.as_view(), name = 'BookAdd'),
    # path('BookList/', BookListView.as_view(), name = 'BookList'),
]