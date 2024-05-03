from django.shortcuts import render, redirect, HttpResponse
from users.models.user import User

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        re_password = request.POST.get('re_pass')
        if email is not None:
            username = email.split('@')[0]
            if password != re_password:
                # messages.warning(request,"Create password and repeat password is not same.Please input same password")
                return redirect('sign_up')
            
            else:
                user_email=User.objects.filter(email=email)
                if user_email.exists():
                    # messages.warning(request,"Email already exist. Try another valid email")
                    return redirect('sign_up')
                else:
                    user =User.objects.create_user(first_name=name,email=email,username=username,password=password)
                    user.is_active=True
                    user.save()
                    return redirect('login')

        else:
            return HttpResponse("problem Register")
    
    
    return render(request, 'home/sign_up.html')