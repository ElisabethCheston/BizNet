from django.shortcuts import render

# Create your views here.

def gig(request):
    """ A view to return the gig page """

    return render(request, 'gig/gig.html')