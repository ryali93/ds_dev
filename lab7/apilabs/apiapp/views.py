import requests

from django.shortcuts import render

from github import Github, GithubException

from .forms import DictionaryForm

# Create your views here.
def oxford(request):
    search_result = {}
    if 'word' in request.GET:
        form = DictionaryForm(request.GET)
        if form.is_valid():
            search_result = form.search()
    else:
        form = DictionaryForm()
    return render(request, 'oxford.html', {'form':form, 'search_result': search_result})



def github(request):
    user = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = "https://api.github.com/users/%s" % username
        response = requests.get(url)
        user = response.json()
    return render(request, 'github.html', {'user':user})


def github_client(request):
    search_result = {}
    if 'username' in request.GET:
        username = request.GET['username']
        client = Github()

        try:
            user = client.get_user(username)
            search_result['name'] = user.name
            search_result['login'] = user.login
            search_result['public_repos'] = user.public_repos
            search_result['success'] = True
        except GithubException as ge:
            search_result['message'] = ge.data['message']
            search_result['success'] = False

        rate_limit = client.get_rate_limit()
        search_result['rate'] = {
            'limit': rate_limit.rate.limit,
            'remaining': rate_limit.rate.remaining,
        }

    return render(request, 'github2.html', {'search_result': search_result})
