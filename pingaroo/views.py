from django.shortcuts import render
from django.views.generic import ListView, DetailView
from pingaroo.models import MonitorTarget


class IndexView(ListView):
    model = MonitorTarget
    template_name = 'index.html'

class ResultView(DetailView):
    model = MonitorTarget
    template_name = 'results.html'