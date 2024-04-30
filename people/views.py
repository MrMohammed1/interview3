from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from .models import Person
from .forms import PersonForm
# Create your views here.



# Create your views here.

# List People
def person_list(request):
    people = Person.objects.all().order_by('name')  # Order by name
    if people:
        context = {'people': people}
        return render(request, 'person_list.html', context)
    else:
        return redirect('person_create')

# Create a Person
class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'person_form.html'
    success_url = '/people/'  # Redirect to person list after creating

# Update a Person
class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'person_form.html'
    success_url = '/people/'  # Redirect to person list after updating

# Delete a Person (consider adding confirmation)
class PersonDeleteView(DeleteView):
    model = Person
    template_name = 'person_delete.html'
    success_url = '/people/'  # Redirect to person list after deleting

# Detail view of a Person (link from person_list.html)
class PersonDetailView(DetailView):
    model = Person
    template_name = 'person_detail.html'
    context_object_name = 'person'

