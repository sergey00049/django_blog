from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length = 125)
    text = models.TextField()
    data = models.DateField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.SET_DEFAULT, default = 'Admin')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', kwargs = {'pk': self.pk})