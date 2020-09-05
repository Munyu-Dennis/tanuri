from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Review


@receiver(post_save)
def create_profile( instance, created, **kwargs):
    if created:
        Review.objects.create()

@receiver(post_save)
def save_profile( instance, **kwargs):
    instance.review.save()
