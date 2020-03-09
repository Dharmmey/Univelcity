from django.shortcuts import render

#LANDING PAGE VIEW
def index(request):
    return render(
        request, 'intro_to_server.html'
    )