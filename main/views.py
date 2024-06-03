from django.shortcuts import render, HttpResponse


# Create your views here.
def get_index(request):
    return render(request, 'main/index.html')


def get_about(request):
    return render(request, 'main/about.html')
