from django.shortcuts import render
from blogs.models import Category,Blog
from tasks.models import About

def home(request):
   # categories=Category.objects.all()
    
    featured_posts=Blog.objects.filter(is_featured=True,status=1).order_by('-updated_at')
    print(featured_posts)
    posts=Blog.objects.filter(is_featured=True,status=1)
    try:
        about=About.objects.get()
    except:
        about=None
    context={
        #'categories':categories,
        'featured_posts':featured_posts,
        'posts':posts,
        'about':about
    }
    return render(request,'home.html',context)

