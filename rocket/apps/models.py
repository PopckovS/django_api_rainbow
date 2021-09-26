from django.db import models


class Example(models.Model):
    """Пример работы модели"""
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to="img/Example", null=True, blank=True, verbose_name='Изображение')

    def __str__(self):
        return f"{self.name} {self.title}"
