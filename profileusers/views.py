from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
# from .models import User

from .models import Profileuser, Industry

# Create your views here.

git def profile(request, username):

	return render(request, 'profileusers/templates/profile.html')
