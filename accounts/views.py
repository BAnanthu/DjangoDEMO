from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User, auth


def sign_up(request):
    if request.method == "GET":
        return render(request, 'signup.html')

    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password == confirm_password:
            if username:
                is_username_exist = User.objects.filter(username=username).exists()
                if is_username_exist:
                    return HttpResponse(f"User with username: {username} already exist!")
            else:
                return HttpResponse(f"username required")

            if email:
                is_email_exist = User.objects.filter(email=email).exists()
                if is_email_exist:
                    return HttpResponse(f"User with email: {email} already exist!")
            else:
                return HttpResponse(f"email required")

            if username and email:
                # save user details
                user_obj = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                return redirect('signin')
        else:
            return HttpResponse("Password does not match.")


def sign_in(request):
    print("working...")
    if request.method == "GET":
        return render(request, 'signin.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('home')
            else:
                return redirect('signin')
        else:
            return HttpResponse(f"email and password required!")


def sign_out(request):
    auth.logout(request)
    return redirect('signin')
