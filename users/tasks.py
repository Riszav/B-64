from time import sleep

from celery import shared_task
from django.core.mail import send_mail


@shared_task
def hello(x):
    print("start task hello")
    sleep(20)

    return f"Hello {x}"


@shared_task
def send_otp_mail(email, code):
    send_mail(
        subject="Your OTP code",
        message=f"code = {code}",
        from_email="B-64-1",
        recipient_list=[email],
    )
    return "OK"


@shared_task
def send_report():
    send_mail(
        subject="[report]",
        message="что то оченб важное",
        from_email="B-64-1",
        recipient_list=[
            "riszav.01@gmail.com",
            "java2geektech@gmail.com",
            "fourdeltaone90@gmail.com",
        ],
    )
    return "OK"
