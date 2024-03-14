from django.urls import path
from.import views 
urlpatterns=[
    path('index/', views.index,name="index"),
    path('register/',views.Register,name="register"),
    path('login/', views.login_user,name="Login"),
    path('logout/', views.logout_user,name="Logout"),
]