from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
def home(request):
	context = {
		"html_var": "eyyyyy"
	}	
	return render(request,"snippets/menu.html",context) # response

class BaseView(TemplateView):
	template_name = "base.html"