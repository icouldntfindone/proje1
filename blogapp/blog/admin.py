from django.contrib import admin
from .models import Blog
from .models import Profile
from .models import Message
from django.contrib.auth.models import User
from .models import Complaint
from .models import Book
from .models import Post
from .models import Comment


from .models import Job



admin.site.register(Job)

admin.site.register(Complaint)





admin.site.register(Profile)
admin.site.register(Book)

admin.site.register(Blog)
admin.site.register(Message)
admin.site.register(Post)
admin.site.register(Comment)








