from django.shortcuts import render

# Create your views here.
def mycard(request):
	return render(request, 'base/mycard.html')

def home(request):
	return render(request, 'base/home.html')
