from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import BlogPost

def myblog(request):
    myblog = BlogPost.objects.order_by('date_added')
    context = {'myblog' : myblog}

    return render(request, 'my_blog.html', context)
