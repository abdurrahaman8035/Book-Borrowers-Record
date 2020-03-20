from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from test_app.forms import RegForm
from .models import Student, Year_Of_Reg, Book

# Create your views here.

file_name = 'static/images/image_name.jpg'

class HomeView(CreateView):
    template_name = 'test app\index.html'
    model = Student
    fields = '__all__'
    initial = {'image_url':file_name}

class Success(ListView):
    template_name = 'test app\students_list.html'
    model = Student
    context_object_name = 'students'
    # total_student = Student.objects.count()
    context = {'total_students':'total_students'}

class BookView(CreateView):
    template_name = 'test app\BookAdd.html'
    model = Book
    fields = ['title','borrowed_by']

class BookListView(ListView):
    template_name = 'test app\BookList.html'
    model = Book
    context_object_name = 'books'
