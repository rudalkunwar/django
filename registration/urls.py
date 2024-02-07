from django.urls import path
from .  import views
urlpatterns = [path('',views.index,name='index'),
               path('about',views.about,name='about'),
               path('login',views.login,name='login'),
               path('register',views.register,name='register'),
               path('signup',views.signup,name='signup'),
               path('blogs',views.blogs,name='blogs'),
               ]