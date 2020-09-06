from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import NoteForm, MarkAsCompletedForm
from .models import Note


# Create your views here.
class Notes(View):
    def get(self, request):
        all_notes = Note.objects.order_by('-deadline')
        context = {
            'notes': all_notes,
        }
        return render(request, 'notes/all_notes.html', context)


class Each_Note(View):
    def get(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        form = MarkAsCompletedForm()
        context = {
            'note': note,
            'form': form
        }
        return render(request, 'notes/note.html', context)

    def post(self, request, pk):
        form = MarkAsCompletedForm(request.POST)
        note = get_object_or_404(Note, pk=pk)
        if form.data['completed'] == "on":
            note.completed = True
        else:
            note.completed = False
        note.save()
        context = {
            'note': note,
            'form': form
        }
        return render(request, 'notes/note.html', context)


class Add_Note(View):
    def get(self, request):
        form = NoteForm()
        return render(request, 'notes/add_note.html', {'form': form})

    def post(self, request):
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('notes:note', pk=note.pk)
        return render(request, 'notes/add_note.html', {'form': form})
