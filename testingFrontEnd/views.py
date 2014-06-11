from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

# Create your views here.
def my_view(request):
	return render(request, 'testingFrontEnd/my_view.html')