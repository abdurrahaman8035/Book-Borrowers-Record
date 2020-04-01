from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView
from .models import Book, Student
from datetime import *
import time
# from .models import Edit_Overdue_Charges
from django.urls import reverse_lazy
from .forms import *

# Create your views here.

def new_book(request, student_id):
    """"Add a new book for a particular student."""
    student = Student.objects.get(id=student_id)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BookForm()
    else:
        # POST data submitted; process data.
        form = BookForm(data=request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.borrowed_by = student
            book.save()
            return redirect('scanner:profile', student_id=student_id)
    # Display a blank or invalid form.
    context = {'student': student, 'form': form}
    return render(request, 'scanner\\addBook.html', context)

def HomeView(request):
    total_books = Book.objects.count()
    total_students = Student.objects.count()
    context = {'total_books':total_books, 'total_students': total_students}
    return render(request, 'scanner\index.html', context)

def StudentDetailView(request, student_id):
   """Show a single student and all books borrowed by students."""
   student = Student.objects.get(id=student_id)
   #get all books borrowed by this student
   all_books = student.books.all()

   for book in all_books:
      # calculate their remaining days left to expire
      current_date = date.today()
      b = datetime.date(book.issued_date)
      days_left = (date(b.year, b.month, b.day) + timedelta(days=14)) - date.today()

      returning_date = date(b.year, b.month, b.day) + timedelta(days=14)
      book.ret_date = returning_date
      result = str(days_left.days) + ' days remaining'
      book.rem_days = result
      book.save()
   books = all_books
   context = {'books': books, 'student': student}
   return render(request, 'scanner\\user_profile.html', context)


class AllStudentsView(ListView):
   model = Student
   template_name = 'scanner\\students_list.html'
   context_object_name = 'students'

class StudentDelete(DeleteView):
    model = Book
    template_name = 'scanner\\deletebook.html'
    #get the student id from the url

    def get_success_url(self):
        student = self.object.borrowed_by.pk
        return reverse_lazy('scanner:profile', kwargs={'student_id': student})