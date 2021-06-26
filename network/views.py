from django.shortcuts import render

# Create your views here.

def network(request):
    """ A view to return the network page """

    return render(request, 'network/network.html')
