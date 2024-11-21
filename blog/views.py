from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Reclamation
from .forms import ReclamationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Liste des réclamations
def reclamation_list(request):
    reclamations = Reclamation.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/reclamation_list.html', {'reclamations': reclamations})


# Détails d'une réclamation
def reclamation_detail(request, pk):
    reclamation = get_object_or_404(Reclamation, pk=pk)
    return render(request, 'blog/reclamation_detail.html', {'reclamation': reclamation})

# Créer une nouvelle réclamation
def reclamation_new(request):
    if request.method == "POST":
        form = ReclamationForm(request.POST)
        if form.is_valid():
            reclamation = form.save(commit=False)
            reclamation.author = request.user
            reclamation.published_date = timezone.now()
            reclamation.save()
            return redirect('reclamation_list')  # Rediriger vers la liste des réclamations
    else:
        form = ReclamationForm()
    return render(request, 'blog/reclamation_edit.html', {'form': form})

# Éditer une réclamation
def reclamation_edit(request, pk):
    reclamation = get_object_or_404(Reclamation, pk=pk)
    if request.method == "POST":
        form = ReclamationForm(request.POST, instance=reclamation)
        if form.is_valid():
            form.save()
            return redirect('reclamation_detail', pk=reclamation.pk)
    else:
        form = ReclamationForm(instance=reclamation)
    return render(request, 'blog/reclamation_edit.html', {'form': form})

# Supprimer une réclamation
@login_required
def reclamation_delete(request, pk):
    reclamation = get_object_or_404(Reclamation, pk=pk)
    reclamation.delete()
    return redirect('reclamation_list')  # Rediriger vers la liste des réclamations

def main_view(request):
    reclamations = Reclamation.objects.all()
    return render(request, 'blog/main.html', {'reclamations': reclamations})