from django.shortcuts import render, redirect
from django.views.generic import ListView,  DeleteView, UpdateView
from .models import Book, Student
from datetime import *
# from .models import Edit_Overdue_Charges
from django.urls import reverse_lazy
from .forms import *
import django_tables2 as tables

# Create your views here.

ADDED_DAYS = 4

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
      b = datetime.date(book.issued_date)
      # a = datetime.date(book.added_days)

      # addedDays = (date(a.year, a.month, a.day))
      #calculate the days left for book to expire
      days_left = (date(b.year, b.month, b.day) + timedelta(days=14)) - date.today()
      returning_date = (date(b.year, b.month, b.day) + timedelta(days=14))

      book.ret_date = returning_date
      result = str(days_left.days) + ' days remaining'
      book.rem_days = result
      book.save()
   books = all_books
   context = {'books': books, 'student': student}
   return render(request, 'scanner\\user_profile.html', context)


class SimpleTable(tables.Table):
    special = tables.URLColumn()
    class Meta:
        model = Student
        fields = ('first_name', 'second_name', 'id_number', 'phone_number', 'registration_date','Email')


class AllStudentsView(tables.SingleTableView, ListView):
    table_class = SimpleTable
    queryset = Student.objects.all()
    model = Student
    template_name = 'scanner\\students_list.html'
    context_object_name = 'students'
    total_students = Student.objects.count()
    extra_context = {'total_students': total_students}

class StudentDelete(DeleteView):
    model = Book
    template_name = 'scanner\\deletebook.html'

    #get the student id from the url
    def get_success_url(self):
        student = self.object.borrowed_by.pk
        return reverse_lazy('scanner:profile', kwargs={'student_id': student})

class RenewBookView(UpdateView):
    model = Book
    fields = ['added_days']
    template_name = 'scanner\\renewbook.html'

    # get the student id from the url
    def get_success_url(self):
        student = self.object.borrowed_by.pk
        return reverse_lazy('scanner:profile', kwargs={'student_id': student})
