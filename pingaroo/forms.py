from django.forms import ModelForm
from pingaroo.models import MonitorTarget

class NewSiteForm(ModelForm):
    class Meta:
        model = MonitorTarget
        fields = ['url']
