from django.shortcuts import render
from .models import URL
import logging
from django.http.response import HttpResponse
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

log = logging.getLogger(__name__)

def index(request):
    return render(request, 'smallify/index.html')

def detail(request):
    try:
        submitted_url = request.POST['original_url']
        if len(submitted_url) <= 0:
            raise URL.DoesNotExist
        
        validate = URLValidator()
        validate(submitted_url)
        
    except(KeyError, URL.DoesNotExist, ValidationError):
        return render(request, 'smallify/index.html', {'error_message' : 'You did not enter a VALID URL !'})
    
    log.info("Submitted url ="+str(submitted_url))
    
    try:
        url = URL.objects.get(original_url = submitted_url)
    except(URL.DoesNotExist):
        url = URL(original_url=submitted_url)
        url.shorten_url()
        url.save()
    
    log.info("Request for url = "+str(url))
    
    return render(request, 'smallify/detail.html', {'url' : url} )


def redirect(request, compressed_url):
    
    try:
        url = URL.objects.get(shortened_url = compressed_url)
    except(URL.DoesNotExist):
        return render(request, 'smallify/index.html', {'error_message' : 'No smallify URL found !'})
    
    res = HttpResponse(url.original_url, status=302)
    res['Location'] = url.original_url
    return res
    
    
    
    
    
    