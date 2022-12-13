from django.urls import path
from emailapp.tasks import index
# get_blog

urlpatterns = [
   path('', index, name='index'),
   # path('cel', get_blog, name='get_blog')
]




