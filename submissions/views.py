from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SubmissionForm

def submit_form(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your submission!')
            form = SubmissionForm()
    else:
        form = SubmissionForm()
    return render(request, 'submissions/submit.html', {'form': form})
