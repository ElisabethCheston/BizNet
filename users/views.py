from django.shortcuts import render

# Create your views here.

def User(request):
    """ A view to return the network page """

    return render(request, 'users/user.html')
