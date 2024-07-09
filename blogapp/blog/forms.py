from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Blog
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView

from .models import Profile
from django import forms
from .models import Message
from django import forms
from django.contrib.auth.models import User
from .models import Message
from .models import Complaint
from django import forms
from .models import Book
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms
from .models import Message
from .models import Job
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms
from .models import Post, Comment

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'requirements', 'location', 'salary','sector']
        


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'content', 'image', 'file']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 2}),
        }




UNIVERSITIES = (
    ('Galatasaray Üniversitesi', 'Galatasaray Üniversitesi'),
    ('İstanbul Teknik Üniversitesi', 'İstanbul Teknik Üniversitesi'),
    ('Orta Doğu Teknik Üniversitesi', 'Orta Doğu Teknik Üniversitesi'),
)

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    password1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'data-toggle': 'password', 'id': 'password'}))
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control', 'data-toggle': 'password', 'id': 'password'}))
    avatar = forms.ImageField(required=False)
    age = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'min': 1, 'max': 120}))
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], required=False)
    university = forms.ChoiceField(choices=UNIVERSITIES, required=False, widget=forms.Select(attrs={'placeholder': 'University', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'avatar', 'age', 'gender', 'university']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            Profile.objects.create(user=user)
        return user
    
    


    

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image']

        


class RegisterForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    
    avatar = forms.ImageField(required=False)
    age = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'min': 1, 'max': 120}))
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], required=False)
    university = forms.ChoiceField(choices=[
        ('Galatasaray Üniversitesi', 'Galatasaray Üniversitesi'),
        ('İstanbul Teknik Üniversitesi', 'İstanbul Teknik Üniversitesi'),
        ('Orta Doğu Teknik Üniversitesi', 'Orta Doğu Teknik Üniversitesi'),
    ], required=False)

    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2','avatar', 'age', 'gender', 'university']
    

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        profile = Profile.objects.create(user=user)  
        return user





class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
                                                                 
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    

    class Meta:
        model = User
        fields = ['username', 'email']



class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], widget=forms.Select(attrs={'class': 'form-control'}), required=False)
    university = forms.ChoiceField(choices=UNIVERSITIES, widget=forms.Select(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Profile
        fields = ['avatar', 'email', 'age', 'gender', 'university']




class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['name', 'email', 'complaint']






class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author', 'pdf', 'summary', 'user_review', 'rating', 'cover_image']

        


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content','sector']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content','image','link']




class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'registration/password_reset_email.html'
    success_url = '/password-reset/done/'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = '/password-reset/complete/'












