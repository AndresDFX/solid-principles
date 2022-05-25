from django.db import models


class Author(models.Model):

    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.email}'


class Book(models.Model):

    name = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, related_name='author_id')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name}'
