import logging

from django.conf import settings
from django.core.mail import send_mail


logger = logging.getLogger(__name__)


def send_contact_request_notification(contact_request):
    """Notify the admin mailbox about a newly submitted contact request."""

    subject = "Новая заявка с сайта HAMMER GYM"
    message = (
        "Новая заявка с сайта:\n\n"
        f"Имя: {contact_request.full_name}\n"
        f"Телефон: {contact_request.phone}\n"
        f"Филиал: {contact_request.get_branch_display()}\n"
        f"Сообщение: {contact_request.message or '-'}\n"
    )

    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_NOTIFICATION_EMAIL],
            fail_silently=False,
        )
    except Exception:
        logger.exception(
            "Не удалось отправить email-уведомление по заявке %s",
            contact_request.pk,
        )
