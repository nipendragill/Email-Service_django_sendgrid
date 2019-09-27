from django.conf.urls import url
urlpatterns = [
    url(r'^send_email/?$', custom_jwt.CustomTokenObtainPairView.as_view(), name='login')
    ]