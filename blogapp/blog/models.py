
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='message_images/', blank=True, null=True)
    file = models.FileField(upload_to='message_files/', blank=True, null=True)
    is_read = models.BooleanField(default=False)  
    def __str__(self):
        return f"From {self.sender.username} to {self.recipient.username} on {self.timestamp}"


    class Meta:
        ordering = ('-timestamp',)



class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    user_review = models.CharField(max_length=255) 
    summary = models.CharField(max_length=500)
    pdf = models.FileField(upload_to='book_pdfs/')  
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    cover_image = models.ImageField(upload_to='images/', blank=True, null=True)



    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class RegisterForm(forms.ModelForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    full_name = forms.CharField(label='Full Name')
    university = forms.ChoiceField()
    
    class Meta:
        model = User  
        fields = ["username", "password1", "password2", "full_name","university"]


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    
    

    def __str__(self):
        return self.title
    
class MyModel(models.Model):
    
    published = models.BooleanField(default=False)




class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)


class Forum(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Thread(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    email = models.EmailField()
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    university = models.CharField(max_length=100, blank=True, choices=[
        ('Galatasaray Üniversitesi', 'Galatasaray Üniversitesi'),
        ('İstanbul Teknik Üniversitesi', 'İstanbul Teknik Üniversitesi'),
        ('Orta Doğu Teknik Üniversitesi', 'Orta Doğu Teknik Üniversitesi'),
    ])

    def __str__(self):
        return self.user.username

    




class Complaint(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    complaint = models.TextField()

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    published_at = models.DateTimeField(auto_now_add=True)
    sector = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    



class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    sector = models.CharField(max_length=100)  

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='comment_images/', blank=True, null=True)  
    link = models.URLField(blank=True, null=True)  

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'





    
    


    






    

    



    
