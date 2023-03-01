from django.shortcuts import render

# Create your views here.
def turnero_index(request):
    return render(request, 'turnero/index.html')