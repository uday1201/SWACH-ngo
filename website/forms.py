from django import forms
from .models import *
from multiupload.fields import MultiFileField

class MotherForm(forms.ModelForm):
	class Meta:
		model = mother
		fields = '__all__'
		widgets = {
        'lmp': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    	}


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['chc'].queryset = chc.objects.none()

		if 'district' in self.data:
			try:
				district_id = int(self.data.get('district'))
				self.fields['chc'].queryset = chc.objects.filter(district_id = district_id).order_by('name')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['chc'].queryset = self.instance.district.chc_set.order_by('name')
		
class UploadForm(forms.Form):
    attachments = MultiFileField(min_num=1, max_num=30, max_file_size=1024*1024*5)