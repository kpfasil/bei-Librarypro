from django.db import models
from django.conf import settings
from django.contrib.auth.models import User 


# Create your models here.

class BookModel(models.Model):
    book_name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    image=models.ImageField(upload_to='book_image',blank=True)
    description=models.CharField(max_length=250)

    def __str__(self):
        return self.book_name

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='user_image')

class IssueBook(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(BookModel,on_delete=models.CASCADE)
    issue_date=models.DateTimeField(auto_now_add=True)
