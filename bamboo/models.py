from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
#    class Meta:
#        ordering = ['name']
    name = models.CharField(verbose_name=u'이름', max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    # author = models.ForeignKey('auth.User')
    writer = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    text = models.TextField()
#    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(Category, null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        'bamboo.Post',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
