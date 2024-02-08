from django.urls import path
from .  import views
urlpatterns = [path('',views.index,name='index'),
               path('about',views.about,name='about'),
               path('login',views.loginpage,name='login'),
               path('register',views.register,name='register'),
               path('signup',views.signup,name='signup'),
               path('signin',views.signin,name='signin'),
               path('signout',views.signout,name='signout'),
               path('blogs/<str:user>',views.blogs,name='blogs'),
               ]