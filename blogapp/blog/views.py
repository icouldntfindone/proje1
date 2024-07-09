from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import AuthenticationForm 
from .forms import RegisterForm
from .forms import BlogForm
from .models import Blog
from .models import Forum
from .models import Complaint
from django.contrib.auth.models import User 
from .models import UserProfile
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from .models import Message
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from .models import User, Message

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message
from django.shortcuts import render, redirect
from .forms import ComplaintForm, BookForm

from .models import Job
from .models import Book
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import JobForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


from django.contrib import messages
from .forms import MessageForm
from .models import Message
from django.contrib.auth.models import User
from django.views import View

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import View
from .forms import RegisterForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm


from .models import Book

def search_books(request):
    query_title = request.GET.get('book_title', '')
    query_author = request.GET.get('author', '')

    if query_title and query_author:
        books = Book.objects.filter(title__icontains=query_title, author__icontains=query_author)
    elif query_title:
        books = Book.objects.filter(title__icontains=query_title)
    elif query_author:
        books = Book.objects.filter(author__icontains=query_author)
    else:
        books = None

    return render(request, 'blog/search_books.html', {'books': books})




def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/jobs/')  
    else:
        form = JobForm()
    return render(request, 'blog/create_job.html', {'form': form})

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'blog/job_list.html', {'jobs': jobs})

def job_sector(request):
    jobs = Job.objects.all()
    return render(request, 'blog/job_sectors.html', {'jobs': jobs})

@login_required
def user_messages(request, username):
    user = User.objects.get(username=username)
    messages = Message.objects.filter(sender=user)
    return render(request, 'blog/user_messages.html', {'user': user, 'messages': messages})



def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            recipient_username = form.cleaned_data['recipient']
            recipient = User.objects.filter(username=recipient_username).first()
            if recipient:
                if recipient != request.user:
                    
                    sender_profile = request.user.profile
                    recipient_profile = recipient.profile
                    if sender_profile != recipient_profile:
                        message = form.save(commit=False)
                        message.sender = request.user
                        message.recipient = recipient
                        
                        message.save()
                        return redirect('inbox')
                    else:
                        messages.error(request, "Kendi profilinize mesaj gönderemezsiniz!")
                else:
                    messages.error(request, "Kendi hesabınıza mesaj gönderemezsiniz!")
            else:
                messages.error(request, f"{recipient_username} adlı kullanıcı bulunamadı.")
    else:
        form = MessageForm()
    return render(request, 'blog/send_message.html', {'form': form})




@login_required
def inbox(request):
    user = request.user
    received_messages = Message.objects.filter(recipient=user).order_by('-timestamp')
 
            
            
                

    context = {
        'received_messages': received_messages,
        
        
    }
    return render(request, 'blog/inbox.html', context)



@login_required
def user_messages(request, username):
    user = get_object_or_404(User, username=username)
    received_messages = Message.objects.filter(recipient=user)
    sent_messages = Message.objects.filter(sender=user)

    context = {
        'user': user,
        'received_messages': received_messages,
        'sent_messages': sent_messages,
    }
    return render(request, 'blog/user_messages.html', context)



    


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('search_books')  
    else:
        form = BookForm()
    return render(request, 'blog/add_book.html', {'form': form})






def user_logout(request):
    logout(request)
    return redirect('main3')



    

def main(request):
    if request.user.is_authenticated:
        return render(request,'blog/main2.html')    
    return render(request,'blog/main.html')




def complaint_form(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('complaint_form')
    else:
        form = ComplaintForm()
    return render(request, 'blog/complaint_form.html', {'form': form})


def iletişim(request):
    return render(request,'blog/iletişim.html')

def main2(request):
    return render(request,'blog/main2.html')

def odtu(request):
    return render(request,'blog/odtu.html')

def itü(request):
    return render(request,'blog/itü.html')

def gsü(request):
    return render(request,'blog/gsü.html')

def odtu_hakkında(request):
    return render(request,'blog/odtu_hakkında.html')

def main3(request):
    return render(request,'blog/main3.html')

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('details',)  
    else:
        form = BlogForm()
    return render(request, 'blog/blog_create.html', {'form': form})

def details(request):
    
    published_blogs =  published_blogs = Blog.objects.all()
    return render(request, 'blog/details.html', {'published_blogs': published_blogs})

def forum_list(request):
    forums = Forum.objects.all()
    return render(request, 'blog/forum_list.html', {'forums': forums})

def forum_detail(request):
    forums = Forum.objects.all()
    return render(request, 'blog/forum_detail.html', {'forums': forums})






def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main2')
            else:
                
                pass  
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})




class RegisterView(View):
    form_class = RegisterForm
    template_name = 'blog/register.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main2')  
        return render(request, self.template_name, {'form': form})

        








class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            
            self.request.session.set_expiry(0)

            
            self.request.session.modified = True

        
        return super().form_valid(form)



class ResetPasswordView(PasswordResetView):
    template_name = 'blog/password_reset.html'
    email_template_name = 'blog/password_reset_email.html'
    subject_template_name = 'blog/password_reset_complete.html'  
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('anasayfa')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'blog/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('anasayfa')

    def form_valid(self, form):
        user = form.save()
        update_session_auth_hash(self.request, user)  
        return super().form_valid(form)


@login_required

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'blog/profile.html', {'user_form': user_form, 'profile_form': profile_form})





def blogdet(request,pk):
    blog = Blog.objects.get(id=pk)
    context = {'blog':blog}
    return render(request,'blog/blog_det.html',context)








def forum_home(request):
    sector = request.GET.get('sector', None)
    if sector:
        posts = Post.objects.filter(sector=sector)
    else:
        posts = Post.objects.all()
    return render(request, 'blog/forum_home.html', {'posts': posts, 'sector': sector})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('forum_home')
    else:
        form = PostForm()

    return render(request, 'blog/new_post.html', {'form': form})




def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            return redirect('password_reset_complete')  
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'blog/password_reset.html', {'form': form})



def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form, 'post': post})






