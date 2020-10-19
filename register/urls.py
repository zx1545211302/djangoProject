from django.urls import path
from . import views


urlpatterns = [
    path('', views.register, name='register'),  # 第一个参数是要去哪才能看到不填就是默认，name起个别名
]
