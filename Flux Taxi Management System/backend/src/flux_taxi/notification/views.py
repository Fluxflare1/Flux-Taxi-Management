from django.core.mail import send_mail

def send_notification(user, subject, message):
    # Placeholder for sending email notifications (to be replaced with push notifications later)
    send_mail(
        subject,
        message,
        'noreply@fluxflare.com',
        [user.email],
        fail_silently=False,
    )
