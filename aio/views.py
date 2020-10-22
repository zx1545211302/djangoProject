from django.shortcuts import render
from . import data


# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        sex = request.POST.get('sex')
        if len(username) <= 20:
            if len(password) <= 25:
                if password.isalnum():
                    if username in data.user_data.keys():
                        error_register_exist = {'error_register_exist': '该用户名已被注册'}
                        return render(request, 'register.html', error_register_exist)
                    else:
                        data.user_data[username] = password
                        data.sex_data[username] = sex
                        success_register = {'success_register': '注册成功,现在请您登陆！'}
                        return render(request, 'login.html', success_register)
                else:
                    error_pass_style = {'error_pass_style': '您输入的密码不是由英文或数字组成！'}
                    return render(request, 'register.html', error_pass_style)
            else:
                error_pass_length = {'error_pass_length': '您输入的密码过长！'}
                return render(request, 'register.html', error_pass_length)
        else:
            error_name_length = {'error_name_length': '您输入的用户名过长！'}
            return render(request, 'register.html', error_name_length)
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username in data.user_data.keys():
            if password == data.user_data[username]:
                success_login = {'success_login': '登陆成功！已跳转到主页！' + '您的性别是' + data.sex_data[username]}
                return render(request, 'index.html', success_login)
            else:
                error_password = {'error_password': '您输入的密码不匹配！'}
                return render(request, 'login.html', error_password)
        else:
            error_username = {'error_username': '您输入的用户名不存在！'}
            return render(request, 'login.html', error_username)
    else:
        return render(request, 'login.html')
