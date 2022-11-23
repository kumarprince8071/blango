from django.shortcuts import render
from django.utils import timezone
from blog.models import Post

# Create your views here.
<<<<<<< HEAD

def index(request):
  posts = Post.objects.filter(published_at__lte = timezone.now())
  return render(request,"blog/index.html", {"posts":post})

=======
def index(request):
  return render(request , "blog/index.html")
>>>>>>> 0244d41efea267bdc250d6bfc974aebb067e82a4
