from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    author_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=3, decimal_places=0)

    def __str__(self):
        return f'id {self.id}: {self.name} ({self.author_name})'
