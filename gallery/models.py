import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Gallery(models.Model):
    # id = models.UUIDField(
    #     primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)

    class Meta:  # new
        indexes = [models.Index(fields=['id'], name='id_index'), ]
        permissions = [('special_status', 'Can read all gallery'), ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gallery_detail', args=[str(self.id)])


class Review(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE,
                                related_name='reviews',)
    review = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self):
        return self.review
