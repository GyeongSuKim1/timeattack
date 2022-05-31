from django.db import models


# Create your models here.
class Article(models.Model):
    class Meta:
        db_table = "Article"

    title = models.CharField(max_length=20, null=False)
    content = models.CharField(max_length=256, null=False)
    category = models.CharField(max_length=256, null=False)


class Category(models.Model):
    category = models.ForeignKey(Article.category, on_delete=models.CASCADE)
    category_title = models.CharField(max_length=20, null=False)
    category_content = models.CharField(max_length=256, null=False)

