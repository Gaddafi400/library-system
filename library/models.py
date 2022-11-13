from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField


class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userprofile")
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = CloudinaryField('image')
    # profile_photo = models.ImageField(upload_to="library/images/profile")

    def __str__(self):
        return self.user.username


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    ISBN = models.CharField(max_length=50)
    revision_number = models.CharField(max_length=50)
    book_title = models.CharField(max_length=255)
    description = models.TextField()
    cover_page = CloudinaryField('image')
    # # cover_page = models.ImageField(upload_to="library/images/coverpage")
    # file = models.FileField(null=True, blank=True, upload_to="library/files")
    file = CloudinaryField('file')
    author = models.ManyToManyField(Author)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publisher_date = models.DateField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.book_title


class BookOutLoan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name="bookoutloan")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date_issue = models.DateField(auto_now=True)
    date_due_for_return = models.DateField()
    date_returned = models.DateField(blank=True, null=True)
    check_out_book = models.BooleanField(default=False)

    def __str__(self):
        return self.book.book_title


class Fine(models.Model):
    amount_fine = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return self.amount_fine


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "contact us"


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)
