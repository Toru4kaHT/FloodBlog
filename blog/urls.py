from django.urls import path, include

from blog.views import RegisterUser, CreateMessageView

# from django.contrib.auth.urls
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', RegisterUser.as_view(), name='register'),
    path('create_message/', CreateMessageView.as_view(), name='create_message')
]