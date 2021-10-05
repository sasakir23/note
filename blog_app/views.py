from blog_app.forms import PostAddForm
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Tag
from .forms import PostAddForm
from django.db.models import Q


def index(request):
   query = request.GET.get('q')
   if query:
       posts = Post.objects.all().order_by('-created_at')
       posts = posts.filter(
       Q(title__icontains=query)|
       Q(user__username__icontains=query)
       ).distinct()
   else:
       posts = Post.objects.all().order_by('-created_at')  
   return render(request, 'blog_app/index.html', {'posts': posts, 'query': query,})


def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog_app/detail.html', {'post': post})

def add(request):
    if request.method == "POST":
        form = PostAddForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('blog_app:index')
    else:
        form = PostAddForm()
    return render(request, 'blog_app/add.html', {'form':form})


def edit(request, post_id):
   post = get_object_or_404(Post, id=post_id)
   if request.method == "POST":
       form = PostAddForm(request.POST, request.FILES, instance=post)
       if form.is_valid():
           form.save()
           return redirect('blog_app:detail', post_id=post.id)
   else:
       form = PostAddForm(instance=post)
   return render(request, 'blog_app/edit.html', {'form': form, 'post':post })


def delete(request, post_id):
   post = get_object_or_404(Post, id=post_id)
   post.delete()
   return redirect('blog_app:index')


def is_valid_q(q):
   return q != '' and q is not None

#関数内の編集
def index(request):
   posts = Post.objects.all().order_by('-created_at')
   title_or_user = request.GET.get('title_or_user')
   date_min = request.GET.get('date_min')
   date_max = request.GET.get('date_max')
   tag = request.GET.get('tag')

   if is_valid_q(title_or_user):
       posts = posts.filter(Q(title__icontains=title_or_user)
                      | Q(user__username__icontains=title_or_user)
                      ).distinct()

   if is_valid_q(date_min):
       posts = posts.filter(created_at__gte=date_min)

   if is_valid_q(date_max):
       posts = posts.filter(created_at__lt=date_max)

   if is_valid_q(tag) and tag != 'タグを選択...':
       posts = posts.filter(tag__tag=tag)
   
   return render(request, 'blog_app/index.html', 
   {'posts': posts, 'title_or_user': title_or_user , 'date_min': date_min, 'date_max': date_max ,'tag': tag})
