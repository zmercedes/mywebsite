from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	html = """<!doctype html>
	<html lang="en">
	<head>
	</head>
	<body>
	<h1> smdftb </h1>
	</body>
	</html>
	"""
	return HttpResponse(html)
	#return render(request,"home.html",{}) # response