from django import forms
from .models import *

class MotherForm(forms.ModelForm):
	class Meta:
		model = mother
		fields = ('name', 'age', 'lmp', 'husband_name', 'district', 'chc', 'village', 'phc', 'asha_name', 'smartphone', 'consent', 'registration_date', 'comment')

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
		
