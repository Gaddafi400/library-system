from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic
from django.conf import settings
from django.db.models import Q

from datetime import date, timedelta

from .forms import CustomUserCreationForm, LoanBookForm, UserProfileModelForm, BookOutLoan
from .models import Book, UserProfile


# CRUD+L - Create, Retrieve, Update and Delete + List


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


class LandingPageView(generic.TemplateView):
    template_name = "library/landing.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("book-list")
        return super().dispatch(request, *args, **kwargs)


def index(request):
    return render(request, template_name='library/index.html')


def book_list_search(request):
    if request.method == 'GET':
        queryset = Book.objects.all()
        return render(request, 'library/book_list.html', {'books': queryset})

    if request.method == 'POST':
        search_field = request.POST.get("search")
        queryset = Book.objects.filter(
            Q(book_title__icontains=search_field) |
            Q(ISBN__icontains=search_field) |
            Q(publisher__name__icontains=search_field))
        return render(request, 'library/book_list.html', {
            'books': queryset,
            'name': search_field

        })


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    queryset = Book.objects.all()
    template_name = "library/book_detail.html"
    context_object_name = "book"


# LOAN BOOK 
class LoanBookListView(LoginRequiredMixin, generic.ListView):
    context_object_name = "borrow_books"
    template_name = "library/loanbook_list.html"

    def get_queryset(self):
        user = self.request.user
        queryset = BookOutLoan.objects.filter(user=user.userprofile.id)
        return queryset


class LoanBookView(LoginRequiredMixin, generic.CreateView):
    # queryset = Book.objects.all()
    form_class = LoanBookForm
    template_name = "library/loan_create.html"

    def get_success_url(self):
        return reverse("book-list")

    def form_valid(self, form):
        current_date = date.today()
        book_borrow = form.save(commit=False)

        book = Book.objects.get(id=self.kwargs["pk"])
        book_borrow.book = book
        book_borrow.user = self.request.user.userprofile
        book_borrow.date_due_for_return = current_date + timedelta(days=10)
        # book_borrow.date_returned = datetime.date.today()
        book_borrow.save()

        send_mail(
            subject="Book Borrowed Notification",
            message=f"You have borrowed {book.book_title} on {current_date} your due to return on {current_date + timedelta(days=10)}",
            from_email="adamu@gmail.com",
            fail_silently=False,
            recipient_list=["gaddafiadamu400@gmail.com"]
        )
        messages.success(self.request, "You have successfully borrow a book")
        return super(LoanBooklView, self).form_valid(form)


class LoanBookDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "library/delete_borrowed_book.html"

    def get_success_url(self):
        return reverse("loan-list")

    def get_queryset(self):
        user = self.request.user
        queryset = BookOutLoan.objects.filter(user=user.userprofile.id)
        return queryset


# USER PROFILE    
class UserProfileListView(LoginRequiredMixin, generic.ListView):
    context_object_name = "userprofile"
    template_name = "library/user_profile.html"

    def get_queryset(self):
        user = self.request.user
        queryset = UserProfile.objects.filter(user=user.userprofile.id)
        return queryset


class UserProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "library/update_user_profile.html"
    form_class = UserProfileModelForm

    def get_success_url(self):
        return reverse("userprofile")

    def get_queryset(self):
        user = self.request.user
        queryset = UserProfile.objects.filter(user=user.userprofile.id)
        return queryset
