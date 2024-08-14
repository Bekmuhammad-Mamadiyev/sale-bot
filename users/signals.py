from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from users.models import Profile,Sale
from users.utils import send_message_tg


User = get_user_model()

@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)


@receiver(post_save, sender = Sale)
def create_sale(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        product.qty -= instance.qty
        product.save()

        if product.qty <10:
            send_message_tg(f'{product.name}ning soni 10 tadan kam qoldi soni {product.qty} ta')
