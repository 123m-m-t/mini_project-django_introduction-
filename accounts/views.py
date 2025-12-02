from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def auth_view(request):
    next_url = request.GET.get("next") or request.POST.get("next")
    if request.method == "POST":
        form_type = request.POST.get("form_type")

        # -------------------
        # SIGNUP
        # -------------------
        if form_type == "signup":
            username = request.POST.get("username")
            password = request.POST.get("password")
            password2 = request.POST.get("password2")

            if password != password2:
                messages.error(request, "Passwords do not match.")
            elif User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password
                )
                user.is_staff = True  # اجازه ورود به admin
                user.is_active = True
                user.save()
                login(request, user)
                return redirect("website:index")

        # -------------------
        # LOGIN
        # -------------------
        elif form_type == "login":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # اگر next هست → همانجا برود
                if next_url:
                    return redirect(next_url)
                return redirect("website:index")
            else:
                messages.error(request, "Invalid username or password.")

    return render(request, "accounts/auth.html")

def logout_view(request):
    logout(request)
    return redirect("/")