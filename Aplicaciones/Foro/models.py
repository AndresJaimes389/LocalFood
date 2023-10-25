from django.db import models
from django.contrib.auth.models import User

# Modelo para representar las categorías del foro
class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

# Modelo para representar los temas (hilos) dentro de una categoría
class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    starter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

# Modelo para representar las publicaciones (respuestas) en un tema
class Post(models.Model):
    message = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return f"Post by {self.created_by.username} in {self.topic.subject}"