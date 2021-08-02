from django.shortcuts import render
from . import views


# Create your views here.

def network(request):
    """ A view to return the network page """

    return render(request, 'network/network.html')


def myContacts(request):
    """ A view to return the My Contacts page """

    return render(request, 'network/contacts.html')


def my_followers(request):
    """ A view to return the My Contacts page """

    return render(request, 'network/my_followers.html')


def following_ppl(request):
    """ A view to return the My Contacts page """

    return render(request, 'network/following_ppl.html')