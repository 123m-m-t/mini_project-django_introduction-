from django.shortcuts import render, HttpResponseRedirect,get_object_or_404
from .models import Newsletter
from blog.models import Post

# Create your views here.

def index_view(request):

    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    return render(request, 'website/contact.html')


def newsletter_view(request):
    if request.method == 'POST':
        email = request.POST.get("email")

        if email:
            Newsletter.objects.get_or_create(email=email)

        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))

