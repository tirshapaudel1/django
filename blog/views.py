from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Post, Category, Comment
from .forms import PostForm

# Create your views here.
#def index(request):
    #return HttpResponse("<h1>Hello my name is trisha</h1>")

def index(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog/home.html', {'posts': posts, 'categories': categories})

def post_detail(request, slug):
    #post = Post.objects.get(slug=slug)
    post = get_object_or_404(Post, slug=slug)
    errors = []
    name =''
    content =''
    
    if request.method == 'POST':
        name = request.POST.get('name', '')
        content = request.POST.get('content', '')
        
        if not name:
            errors.append('Name is required.')
        elif len(name) >= 100:
            errors.append('Name is too long.')
        if not content:
            errors.append('Content is required.')
        
        if not errors:
            Comment.objects.create(post=post, name=name, content=content)
            redirect('blog:post_detail', slug=post.slug)
    
    return render(request, 'blog/post_detail.html', 
    {
        'post': post,
        'errors': errors,
        'name': name,
        'content': content
        })

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm()
    
    return render(request, 'blog/post_create.html', {'form': form})

def about(request):
    return HttpResponse("<h1>I study at texas</h1>")

def post_list(request):
    query = request.GET.get('q', '')
    posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    context = {
        'posts': posts,
        'query': query,
    }
    return render(request, 'blog/post_list.html', context)
