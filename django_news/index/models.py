from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=256)

    def __str__(self):
        return str(self.category_name)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

class Product(models.Model):
    product_name = models.CharField(max_length=512)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_des = models.TextField(blank=True)
    product_photo = models.ImageField(upload_to='media')

    def __str__(self):
        return str(self.product_name)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

