from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .forms import InserationForm
from .models import Inseration


def insert_view(request):
    context = {}
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    if request.method == "POST":
        insert_form = InserationForm(request.POST, request.FILES)
        if insert_form.is_valid():
            form = insert_form.save(commit=False)
            form.inserter = request.user
            form.save()
            return redirect('index')
    else:
        insert_form = InserationForm()
    context['insert_form'] = insert_form
    return render(request, 'inseration/insert.html', context)

def view_inseration(request, inseration_id):
    context = {}
    inseration = get_object_or_404(Inseration, pk=inseration_id)
    context['inseration'] = inseration
    return render(request, 'inseration/view_inseration.html', context)
