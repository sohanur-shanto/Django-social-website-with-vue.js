from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Oink
from django.contrib.auth.models import User

@login_required
def feed(request):
    userids = [request.user.id]

    for oinker in request.user.oinkerprofile.follows.all():
        userids.append(oinker.user.id)
    
    oinks = Oink.objects.filter(created_by_id__in= userids)

    context = {
        'oinks': oinks,
    }

    return render(request, 'feed/feed.html', context)

@login_required
def search(request):
    query = request.GET.get('query', '')

    if len(query) > 0:
        oinkers = User.objects.filter(username__icontains = query)
    else:
        oinkers = []

    context = {
        'query' : query,
        'oinkers' : oinkers,
    }

    return render(request, 'feed/search.html', context)
