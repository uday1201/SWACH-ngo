from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from website.models import mother
from django.views.generic.edit import FormView
from .forms import UploadForm
from .models import Attachment

# Create your views here.
class MotherListView(ListView):
	model = mother
	context_object_name = 'mother'

class MotherCreateView(CreateView):
	model = mother
	fields = ('name', 'age', 'lmp', 'husband_name', 'district', 'chc', 'village', 'phc', 'asha_name', 'smartphone', 'consent', 'registration_date', 'comment')
	success_url = reverse_lazy('mother_changelist')

class MotherUpdateView(UpdateView):
	model = mother
	fields = ('name', 'age', 'lmp', 'husband_name', 'district', 'chc', 'village', 'phc', 'asha_name', 'smartphone', 'consent', 'registration_date', 'comment')
	success_url = reverse_lazy('mother_changelist')

'''def load_chc(request):
    district_id = request.GET.get('district')
    chc = chc.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'hr/chc_dropdown_list_options.html', {'chc': chc})'''

class UploadView(FormView):
    template_name = 'website/form.html'
    form_class = UploadForm
    success_url = '/done/'

    def form_valid(self, form):
        for each in form.cleaned_data['attachments']:
            Attachment.objects.create(file=each)
        return super(UploadView, self).form_valid(form)