from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
                # Redirect to a success page.
            return redirect('conversation')
        
    return render(request, 'home/login.html')