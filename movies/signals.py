from django.db.models.signals import post_delete
from django.core.mail import send_mail
from django.dispatch import receiver
from .models import movie

@receiver(post_delete, sender=movie)
def my_handler(*args, **kwargs):
    print(args)
    print(kwargs)
    # send_mail('Mail Subject', 'Mail Body',
    #           'muhame732@gmail.com', ['muhame948@gmail.com', ], fail_silently=False
    #           )