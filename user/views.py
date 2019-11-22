from django.shortcuts import render, redirect
from .forms import UserOurRegistration
from django.contrib.auth.decorators import login_required
from blog.models import Post

def register(request):
    if request.method == 'POST':
        form = UserOurRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserOurRegistration()

    return render(request, 'user/registration.html', {'form': form, 'title': 'Регистрация'})

@login_required
def profile(request):
    data = {
        'posts': Post.objects.filter(author = request.user),
        'count': len(Post.objects.filter(author = request.user)),
        'title': 'Профиль'
    }
    return render(request, 'user/profile.html', data)