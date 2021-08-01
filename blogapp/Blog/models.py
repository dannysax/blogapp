from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
   

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status="published")


    options = (
        ("published", "Published"),
        ("draft", "Draft")
    )

    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    published = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=250, unique_for_date='published')
    status = models.CharField(max_length=10, choices=options, default="published")
    objects = models.Manager() #default manager
    postobjects = PostObjects() #Custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title