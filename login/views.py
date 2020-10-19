from django.shortcuts import render
from djangoProject import data

# Create your views here.
happy = 'happy'


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username in data.user_data.keys():
            if password == data.user_data[username]:
                return render(request, 'index.html')
            else:
                pass
                #密码错误
        else:
            pass
            #用户名不存在
    else:
        return render(request, 'login.html')