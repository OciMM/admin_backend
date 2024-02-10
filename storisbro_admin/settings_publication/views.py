from django.shortcuts import render, redirect
from .forms import PublicationSettingsForm
from .models import PublicationSettings

def change_publication_order(request, settings_id):
    settings = PublicationSettings.objects.get(pk=settings_id)

    if request.method == 'POST':
        form = PublicationSettingsForm(request.POST, instance=settings)
        if form.is_valid():
            form.save()
            return redirect('your_redirect_url')  
    else:
        form = PublicationSettingsForm(instance=settings)

    return render(request, 'change_publication_order.html', {'form': form})