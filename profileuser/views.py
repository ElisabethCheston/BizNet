from django.shortcuts import render

# Create your views here.

def profileuser(request):
    """ A view to return the profileuser page """

    return render(request, 'profileuser/profileuser.html')