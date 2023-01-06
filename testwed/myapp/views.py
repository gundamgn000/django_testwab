from django.shortcuts import render

# Create your views here.

from django.http.response import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("My First Django App.") 

from django.template.loader import get_template
from .models import Post
from datetime import datetime
# Create your views here.
def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    post_lists = list()
    for count, post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count)) +str(post)+"<br>")
        post_lists.append("<small>"+str(post.body)+"</small><br><br>")
    return render(request, 'index.html', locals())

from django.shortcuts import redirect

def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')    