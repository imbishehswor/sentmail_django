# import email
# from django.http import HttpResponse
# from django.shortcuts import render
# from django.core.mail import EmailMessage
# from django.conf import settings
# from django.template.loader import render_to_string
# from django.core.mail import send_mail


# Create your views here.




# def success(request):

#     send_mail(

#         'Testing mail',
#         'Here is the message for test.',
#         'bisheshwor.khadka@apexcollege.edu.np',
#         ['rohan.shrestha19@apexcollege.edu.np'],
#         fail_silently=False,
        
#     )

  
#     print("sucessful")
    


       # return render(request, "success.html")

    # return HttpResponse('succes')
      # email = EmailMessage(
    #     'subject',
    #     'body',
    #     settings.EMAIL_HOST_USER,
    #     ['bisheshwor.khadka@apexcollege.edu.np'],
    # )
    # email.fail_silently = False
    # email.send()


from random import random
from django.core import mail
from django.http import HttpResponse
from django.conf import settings
import random


def success(request):

    connection = mail.get_connection()

    connection.open()

    n = random.randint(111111,999999)
    cn = str(n)
    email1 = mail.EmailMessage(
        'Email verification ',
        " Dear User, \n          This is system generated Email please do not reply to this Email ID.  \n\n OTP Code:"+cn+"\n\n\n\n\n BEST REGARDS, \n Bisheshwor Khadka",
        'bisheshwor.khadka@apexcollege.edu.np',
        ['kbibash2058@gmail.com'],
        connection=connection,
    )

    email1.send()

    connection.close()

    print("success")
    return HttpResponse("hello")

