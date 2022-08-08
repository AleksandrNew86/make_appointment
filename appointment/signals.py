from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Appointment
from django.core.mail import mail_managers


@receiver(post_save, sender=Appointment)
def notify_managers_appointment(sender, instance, created, **kwargs):
    if created:
        subject = f'{instance.client_name} {instance.date.strftime("%Y-%m-%d")}',
    else:
        subject = f'Appointment {instance.client_name} in {instance.date.strftime("%Y-%m-%d")} was changed'
    mail_managers(
        subject=subject,
        message=instance.message,
    )


@receiver(post_delete, sender=Appointment)
def notify_managers_appointment(sender, instance, **kwargs):
    subject = f'Appointment {instance.client_name} in {instance.date.strftime("%Y-%m-%d")} was deleted'
    mail_managers(
        subject=subject,
        message=subject,
    )
