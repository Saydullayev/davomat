from django.shortcuts import redirect, render
from .models import *
from .algorithms import *

ish_xona_r = 70 # ish xona binosini radiuse, ish xona quyilgan nuqtaga 20 metr yaqinlashsa ish xonada deb hisoblaydi
ish_xona_x =  39.6513963
ish_xona_y = 66.9653502


def profile(r):
    login = r.session.get('login')
    if login:
        password = r.session.get('password')
        if User.objects.filter(login=login, password=password):
            user = User.objects.get(login=login, password=password)
            if r.method=="POST":
                lat = float(r.POST.get('lat'))
                long = float(r.POST['long'])
                distance = calculate_distance(lat, long, ish_xona_x, ish_xona_y)
                print(distance)
                if distance < ish_xona_r:
                    user.ishdami = True
                    user.save()
            return render(r, 'profile.html', {'ism': user.ism, 'familiya': user.familiya, 'ishdami': user.ishdami, 'x':ish_xona_x, 'y':ish_xona_y})
        else:
            return redirect('/login')
    else:
        return redirect('/login')

def login(r):
    if r.method == "POST":
        login = r.POST.get('login')
        password = r.POST.get('password')
        print(login, password)
        if User.objects.filter(login=login, password=password):
            user = User.objects.get(login=login, password=password)
            r.session['login'] = user.login
            r.session['password'] = user.password
            return redirect('/')
        else:
            return redirect('/login')
    return render(r, 'login.html')