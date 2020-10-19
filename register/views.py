from django.shortcuts import render
from djangoProject import data

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username in data.user_data.keys():

        else:
            data.user_data[username] = password

    else:
        return render(request, 'register.html')
