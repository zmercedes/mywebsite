from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .models import Project

class BaseView(TemplateView):
	template_name = "base.html"