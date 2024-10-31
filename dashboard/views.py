from django.shortcuts import render

# Create your views here.
def index_dashboard(request):
    context = {
        'title': 'Dashboard'
    }
    return render(request, 'dashboard/index.html', context)
