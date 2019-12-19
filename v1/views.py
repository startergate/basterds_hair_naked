from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello World!")


def get_profile(request, pid):
    return JsonResponse({
        "pid": pid,
        "total": {
            "score": 10000000,
            "playtime": 42342423,
            "turn_count": 8000,
            "match_count": 1000,
            "win_count": 500,
            "spawned_alias": 10000,
            "killed_alias": 12000,
            "killed_hostiles": 10000,
            "damage": 3000000,
            "heal": 250000
        },
        "1": {
            "score": 10000000,
            "playtime": 42342423,
            "turn_count": 8000,
            "match_count": 1000,
            "win_count": 500,
            "spawned_alias": 10000,
            "killed_alias": 12000,
            "killed_hostiles": 10000,
            "damage": 3000000,
            "heal": 250000
        },
        "2": {
            "score": 10000000,
            "playtime": 42342423,
            "turn_count": 8000,
            "match_count": 1000,
            "win_count": 500,
            "spawned_alias": 10000,
            "killed_alias": 12000,
            "killed_hostiles": 10000,
            "damage": 3000000,
            "heal": 250000
        },
        "3": {
            "score": 10000000,
            "playtime": 42342423,
            "turn_count": 8000,
            "match_count": 1000,
            "win_count": 500,
            "spawned_alias": 10000,
            "killed_alias": 12000,
            "killed_hostiles": 10000,
            "damage": 3000000,
            "heal": 250000
        }
    })


def get_match(request, match_id):
    return JsonResponse({})


def get_match_specific(request, match_id, pid):
    return JsonResponse({})
