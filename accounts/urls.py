from django.urls import path

from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    #ez jelenti azt hogy 127.0.stb/signup-on lesz
   
    
    
]
