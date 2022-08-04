from django.urls import path,include
from . import views

app_name = 'registerApp'

urlpatterns = [
    path('',views.index,name ="index"),
    path('register/',views.register,name ="register"),
    path('login/',views.userLogin,name ="login"),
    path('logout/',views.userLogout,name ="logout"),
]
