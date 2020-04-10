from django.db import models


class TestPage(models.Model):
    content1 = models.TextField()
    content2 = models.TextField()


class TestInline(models.Model):
    page = models.ForeignKey(TestPage, on_delete=models.CASCADE)
    content1 = models.TextField()
    content2 = models.TextField()
