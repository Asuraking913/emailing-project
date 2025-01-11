from django.shortcuts import render
from django.core.mail import send_mail
from email_example.settings import EMAIL_HOST_USER


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

    if request.method == "POST":
        sender_name = request.POST.get("name")
        sender_email = request.POST.get("email")
        sender_sms = request.POST.get("sms")

        print(EMAIL_HOST_USER)

        send_mail(
            f"Test email from {EMAIL_HOST_USER}",
            f"{sender_sms}",
            f"{EMAIL_HOST_USER}",
            [f"{sender_email}"],
            fail_silently=False,
        )

    return render(request, "index.html")
