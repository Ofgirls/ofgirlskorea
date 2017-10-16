from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
#    class Meta:
#        ordering = ['name']
    name = models.CharField(verbose_name=u'이름', max_length=50)
    slug = models.SlugField(unique=True, null=True, blank=True)
    description = models.TextField(verbose_name=u'말머리 설명', blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    # author = models.ForeignKey('auth.User', null=True)
    writer = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    text = models.TextField()
#    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(Category, default=1, blank=True)
    post_password = models.CharField(verbose_name=u'password', max_length=100, default='', help_text="글을 수정하거나 지울 때 사용할 비밀번호를 적어주세요")

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
