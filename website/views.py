from django.shortcuts import render, HttpResponseRedirect,get_object_or_404,redirect
from .models import Newsletter
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url="/accounts/auth/?form_type=login")
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("website:contact")  # یا صفحه موفقیت
    else:
        form = ContactForm()

    return render(request, "website/contact.html", {"form": form})
def index_view(request):

    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')


@login_required(login_url="/accounts/auth/?form_type=login")
def newsletter_view(request):
    if request.method == 'POST':
        email = request.POST.get("email", "").strip()

        if not email:
            messages.error(request, "Email cannot be empty.")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))

        obj, created = Newsletter.objects.get_or_create(email=email)

        if created:
            messages.success(request, "You have successfully subscribed.")
        else:
            messages.info(request, "You are already subscribed.")

        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))

