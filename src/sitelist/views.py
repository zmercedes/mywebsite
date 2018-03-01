from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .models import Project

def BaseView(request):
	template_name = "content.html"
	queryset = Project.objects.all()
	return render(request,template_name, { "project_list" : list(queryset) })
