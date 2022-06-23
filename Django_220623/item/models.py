from datetime import timezone
from distutils.command.upload import upload
import os
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class Category(models.Model):
    name = models.CharField("이름", max_length=30)

    def __str__(self):
        return self.name


class Items(models.Model):
    name = models.CharField("이름", max_length=30)
    image_url = models.ImageField(upload_to="%Y/%m/%d")
    category = models.ManyToManyField(Category, verbose_name=("category"))

    def date_upload_to(instance, filename):
  # upload_to="%Y/%m/%d" 처럼 날짜로 세분화
        ymd_path = timezone.now().strftime('%Y/%m/%d') 
        # 길이 32 인 uuid 값
        uuid_name = uuid4().hex
        # 확장자 추출
        extension = os.path.splitext(filename)[-1].lower()
        # 결합 후 return
        return '/'.join([
            ymd_path,
            uuid_name + extension,
        ])

        photo = models.ImageField(upload_to=date_upload_to)
    
    def __str__(self):
        return self.name