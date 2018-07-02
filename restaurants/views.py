from django.shortcuts import render

# Create your views here.
def view_render(request):
	context = {'msg': 'Hello World!'}
	return render (request,"fawaz.html", context)