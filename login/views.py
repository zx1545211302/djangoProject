from django.shortcuts import render
from djangoProject import data


# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username in data.user_data.keys():
            if password == data.user_data[username]:
                success_login = {'success_login': '登陆成功！已跳转到主页！'}
                return render(request, 'index.html', success_login)
            else:
                error_password = {'error_password': '您输入的密码不匹配！'}
                return render(request, 'login.html', error_password)
        else:
            error_username = {'error_username': '您输入的用户名不存在！'}
            return render(request, 'login.html', error_username)
    else:
        return render(request, 'login.html')
