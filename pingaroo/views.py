from django.http import JsonResponse
from django.views.generic import ListView, DetailView, FormView
from pingaroo.models import MonitorTarget
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from pingaroo.forms import NewSiteForm

class IndexView(LoginRequiredMixin, ListView):
    model = MonitorTarget
    template_name = 'index.html'

    def get_queryset(self):
        return MonitorTarget.objects.filter(user=self.request.user)

class ResultView(LoginRequiredMixin, DetailView):
    model = MonitorTarget
    template_name = 'results.html'


class SitesView(LoginRequiredMixin, ListView):
    model = MonitorTarget
    template_name = 'sites.html'

class NewSiteView(LoginRequiredMixin, FormView):
    template_name = 'new_site.html'
    form_class = NewSiteForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save(request.user)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class LoginView(LoginView):
    success_url = '/'

def foo_api_view(request):
    json_payload = []
    targets = MonitorTarget.objects.filter(user=request.user)
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