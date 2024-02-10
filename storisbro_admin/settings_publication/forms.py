from django import forms
from .models import PublicationSettings

class PublicationSettingsForm(forms.ModelForm):
    class Meta:
        model = PublicationSettings
        fields = ['publication_order', 'time_interval_between_publications']