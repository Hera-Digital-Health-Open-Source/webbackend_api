import logging
from datetime import timedelta

from django.db.models.signals import post_save
from django.dispatch import receiver
import django
from django.core.exceptions import ObjectDoesNotExist

from events.models import NotificationEvent, InstantNotification
from events.utils import send_notification
from django.contrib.auth.models import User


logger = logging.getLogger(__name__)


@receiver(post_save, sender=NotificationEvent)
def send_notification_to_onesignal(sender, instance: NotificationEvent, **kwargs):
    if instance.push_notification_sent_at is not None:
        return

    response = send_notification(instance.push_title, instance.push_body, [instance.user.username])

    if 200 <= response.status_code <= 299 and 'errors' not in response.body:
        instance.push_notification_sent_at = django.utils.timezone.now()
        instance.save()
    else:
        logger.error(f"Error when sending notification event {instance.id} to OneSignal: {response.body}")


@receiver(post_save, sender=InstantNotification)
def send_instant_notification_to_onesignal(sender, instance: InstantNotification, **kwargs):
    now = django.utils.timezone.now()
    expires = now + timedelta(days=1)
    for num in instance.phone_numbers:
        user = User.objects.get(username=num)
        try:
            user.userprofile
        except ObjectDoesNotExist:
            logger.error("User doesn't have profile")
            continue

        notification_event = NotificationEvent(user=user, notification_type=instance.notification_type, notification_available_at=now, notification_expires_at=expires)
        notification_event.save()
