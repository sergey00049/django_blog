from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class ShowPostView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    ordering = ['-data']
    paginate_by = 5

    def get_context_data(self, **kwards):
        ctx = super(ShowPostView, self).get_context_data(**kwards)
        ctx['title'] = 'Главная страница'
        return ctx

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'text'] 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author or self.request.user == 'sergey':
            return True
        return False

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwards):
        import random
        ctx = super(PostDetailView, self).get_context_data(**kwards)
        ctx['title'] = Post.objects.filter(pk = self.kwargs['pk'])[0]

        random1 = random.randrange(len(Post.objects.all()))
        random2 = random.randrange(len(Post.objects.all()))
        while random1 == random2:
            random2 = random.randrange(len(Post.objects.all()))
            
        posts = [ 
            Post.objects.all()[random1], 
            Post.objects.all()[random2]
        ]
        ctx['posts'] = posts
        return ctx

class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author or self.request.user == 'sergey':
            return True
        return False

def show_my_post(request):
    data = {
        'posts': Post.objects.filter(author = request.user).order_by('-data'),
        'title': 'Ваши посты'
    }
    return render(request, 'blog/blog.html', data)