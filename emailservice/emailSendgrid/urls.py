from django.conf.urls import url
from .views import SendEmailView
urlpatterns = [
    url(r'^send_email/?$', SendEmailView.as_view(), name='login')
    ]