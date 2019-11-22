from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowPostView.as_view(), name='main'),
    path('posts/add', views.CreatePostView.as_view(), name = 'add'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name = 'detail'),
    path('posts/<int:pk>/update/', views.UpdatePostView.as_view(), name = 'update'),
    path('posts/<int:pk>/delete', views.DeletePostView.as_view(), name = 'delete'),
    path('my_posts/', views.show_my_post, name = 'my_posts')
]