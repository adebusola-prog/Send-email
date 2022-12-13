from django.shortcuts import render
from .models import MyEmail
from django.http import JsonResponse  
from emailapp.tasks import sleep_well
from django.core.mail import send_mail
# Create your views here.


# def index(request):
#    list_email= list(MyEmail.objects.all())
#    print(list_email)
#    send_mail(
#       'Hey, sending from meeee',
#       "Yop, it's close",
#       'adebusolayeye@gmail.com',
#       list_email,
#       fail_silently=False)
#    sleep_well()
#    return render(request, 'emailapp/index.html')

#  getting your ip_address

# def get_ip_address(request):
#    user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
#    if user_ip_address:
#       ip = user_ip_address.split(',')[0]
#    else:
#       ip = request.META.get('REMOTE_ADDR')
#    return ip

# def show_ip_address(request):
#    user_ip = get_ip_address(request)
#    return render(request, "emailapp/output.html", {"user_ip":user_ip})


def get_blog(request):
   data = {
      'success': True,
      'message': 'simple api response'
   }
   sleep_well(5)
   return JsonResponse(data)