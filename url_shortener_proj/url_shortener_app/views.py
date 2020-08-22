from django.shortcuts import render, get_object_or_404, redirect

from .models import UrlModel
# Create your views here.

def redirection(request, url_hash):
    """
    The function gets the hashed_url and redirects to the main url
    """
    url = get_object_or_404(UrlModel, hashed_url=url_hash)
    # add stats
    url.add_url_click()
    # redirect to main url
    return redirect(url.url)