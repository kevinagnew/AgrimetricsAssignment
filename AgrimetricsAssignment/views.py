from django.shortcuts import render


# Request for home_view
def home_view(request):
    return render(request, 'homepage.html')
