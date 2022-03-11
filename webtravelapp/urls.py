from django.urls import path
from django.urls.resolvers import URLPattern
from.import views 
urlpatterns=[
    path('',views.web,name='web'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('getone',views.getone,name='getone'),
    path('message',views.message,name='message'),
    path('register',views.register,name='register'),
    path('regi',views.regi,name='regi'),
    path('registrations',views.registrations,name='registrations'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('userin',views.userin,name='userin'),
    path('logout',views.logout,name='logout')
    
]