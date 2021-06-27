from django.shortcuts import render

# Create your views here.

def settings(request):
    """ A view to return the settings page """

    return render(request, 'home/settings.html')