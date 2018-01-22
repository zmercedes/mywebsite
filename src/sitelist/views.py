from django.shortcuts import render

# Create your views here.
def home(request):
	context = {
		"html_var": "eyyyyy"
	}	
	return render(request,"snippets/menu.html",context) # response