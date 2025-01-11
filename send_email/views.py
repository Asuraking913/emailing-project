from django.shortcuts import render
from django.core.mail import send_mail


def send_email(sender, receiver):
    send_mail(
        "Hello From Asura's Testing codes",
        f"Hello there, you just received an automated email from {sender}",
        f"{sender}",
        [f"{receiver}"],
        fail_silently=False,
    )


# Create your views here.
def index(request):

    # send_email("emailtesting913@gmail.com", "israelshedrack913@gmail.com")
    send_mail(
        "Hello From Asura's Testing codes",
        f"Hello there , you just received an automated email from israelshedrack913@gmail.com",
        "emailtesting913@gmail.com",
        ["emailtesting913@gmail.com"],
        fail_silently=False,
    )

    return render(request, "index.html")
