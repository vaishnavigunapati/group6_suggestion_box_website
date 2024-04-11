from django.shortcuts import render, redirect
from .models import Suggestion
from .forms import SuggestionForm

def suggestion_list(request):
    suggestions = Suggestion.objects.all()
    return render(request, 'suggestions/suggestion_list.html', {'suggestions': suggestions})

def suggestion_submit(request):
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suggestion_list')
    else:
        form = SuggestionForm()
    return render(request, 'suggestions/suggestion_submit.html', {'form': form})
