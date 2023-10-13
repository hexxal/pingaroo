from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from pingaroo.models import MonitorTarget


class IndexView(ListView):
    model = MonitorTarget
    template_name = 'index.html'

class ResultView(DetailView):
    model = MonitorTarget
    template_name = 'results.html'

def foo_api_view(request):
    json_payload = []
    targets = MonitorTarget.objects.all()
    for target in targets:
        # TODO: Perffi. Cache jne. rajotetaan vähän maksimiresultteja.
        # TODO: Login
        latencies = [target.latency for target in target.results.all() if target.latency is not None][:20]
        foo = {
            'url': target.url,
            'results': {'series': [{'data': latencies}]}
        }
        json_payload.append(foo)
    return JsonResponse(json_payload, safe=False)