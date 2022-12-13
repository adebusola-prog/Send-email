from celery import shared_task
from time import sleep
from django.shortcuts import render
from django.core.mail import send_mail
from .models import MyEmail

@shared_task
def sleep_well(duration):
   print('Sleeping for {0} seconds'.format(duration))
   sleep(duration)

@shared_task
def index(request):
   list_email= list(MyEmail.objects.all())
   print(list_email)
   send_mail(
      'Hey, sending from meeee',
      "Yop, it's close",
      'adebusolayeye@gmail.com',
      list_email,
      fail_silently=False)
   # sleep_well(duration)
   return render(request, 'emailapp/index.html')