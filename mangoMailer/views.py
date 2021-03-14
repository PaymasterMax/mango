from django.shortcuts import render
from django.core.mail import send_mail,send_mass_mail
import re
def sendEmails(request):
    if request.method == "POST":
        # emails = ["duncansantiago18@gmail.com","dalmasogembo@gmail.com","nekoerick2@gmail.com","anornymous99@gmail.com",
        # "magangimoffat@gmail.com","cshamaldas@gmail.com"]
        emails = request.POST.get('emails')
        message = request.POST.get('message')
        # print(re.search('[a-zA-Z0-9]+', emailslist,"gi"))
        emaillist = emails.split(';')
        for email in emaillist:
            print(email)

        return render(request, "mailer.html",context = {})

    # for email in emails:
    #     res = send_mail("Account activation"," please reset your account here ",email,[email],fail_silently = False)
    return render(request, "mailer.html",context = {})
