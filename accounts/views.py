from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, SignupForm


def auth_view(request):
    next_url = request.GET.get("next") or request.POST.get("next")

    login_form = LoginForm()
    signup_form = SignupForm()

    if request.method == "POST":
        form_type = request.POST.get("form_type")

        # -------------------
        # SIGNUP
        # -------------------
        if form_type == "signup":
            signup_form = SignupForm(request.POST)

            if signup_form.is_valid():
                user = User.objects.create_user(
                    username=signup_form.cleaned_data["username"],
                    password=signup_form.cleaned_data["password"]
                )
                user.is_staff = True
                user.is_active = True
                user.save()

                login(request, user)
                messages.success(request, "You have successfully signin.")
                return redirect("website:index")
            else:
                for error in signup_form.errors.values():
                    messages.error(request, error)

        # -------------------
        # LOGIN
        # -------------------
        elif form_type == "login":
            login_form = LoginForm(request.POST)

            if login_form.is_valid():
                user = authenticate(
                    request,
                    username=login_form.cleaned_data["username"],
                    password=login_form.cleaned_data["password"]
                )

                if user:
                    login(request, user)
                    messages.success(request, "You have successfully logged in.")
                    return redirect(next_url or "website:index")
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                for error in login_form.errors.values():
                    messages.error(request, error)

    return render(request, "accounts/auth.html", {
        "login_form": login_form,
        "signup_form": signup_form,
    })


def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect("/")
