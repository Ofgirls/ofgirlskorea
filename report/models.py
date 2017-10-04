from django.db import models
from django.utils import timezone


# Create your models here.
class Report(models.Model):
    author = models.ForeignKey('auth.User')
    # 우리의 플젝에선 models.CharField를 제일 많이 쓸 듯.
    # model의 필드 정의 참고:  https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-types

    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
