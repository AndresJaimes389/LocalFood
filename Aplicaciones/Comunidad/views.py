from django.shortcuts import render, redirect
from .forms import ThreadForm
from django.contrib.auth.decorators import login_required

@login_required
def create_thread(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.user = request.user
            thread.save()
            return redirect('create_thread')  # Redirige a la página principal del foro
    else:
        form = ThreadForm()
    return render(request, 'create_thread.html', {'form': form})

