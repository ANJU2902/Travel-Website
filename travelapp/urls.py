from django.urls import path
from django.urls.resolvers import URLPattern
from.import views
urlpatterns=[
    path('travel',views.travel,name='travel'),
    path('destination',views.destination,name='destination'),
    path('view',views.view,name='view'),
    path('getdata',views.getdata,name='getdata'),
    path('edit/<int:sid>/',views.edit,name='edit'),
    path('delete/<int:vid>/',views.delete,name='delete'),
    path('update/<int:wid>/',views.update,name='update'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('adlogin',views.adlogin,name='adlogin')
]