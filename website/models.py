from djongo import models
from django.utils import timezone

# Create your models here.
class asha(models.Model):
	name = models.CharField(max_length=150)
	phone_number = models.CharField(max_length=13)

	def __str__(self):
		return self.name

class district(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class chc(models.Model):
	district = models.ForeignKey(district, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class village(models.Model):
	chc = models.ForeignKey(chc, on_delete = models.CASCADE)
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class phc(models.Model):
	village = models.ForeignKey(village, on_delete = models.CASCADE)
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class mother(models.Model):
	#key
	name = models.CharField(max_length=150)
	age = models.IntegerField()
	lmp = models.DateField()
	husband_name = models.CharField(max_length=150)
	district = models.ForeignKey(district, on_delete=models.SET_NULL, null=True)
	chc = models.ForeignKey(chc, on_delete=models.SET_NULL, null=True)
	village = models.ForeignKey(village, on_delete=models.SET_NULL, null=True)
	phc = models.ForeignKey(phc, on_delete=models.SET_NULL, null=True)
	asha_name = models.OneToOneField(asha, on_delete=models.CASCADE)
	smartphone = models.BooleanField()
	consent = models.BooleanField()
	registration_date = models.DateTimeField(default = timezone.now)
	comment = models.TextField()

	def __str__(self):
		return self.name

class child(models.Model):
	delivery_date = models.DateField()
	#delivery_place = models.CharField(max_length=100)
	baby_status = models.CharField(max_length=100)
	#birth_type = models.CharField(max_length=100)
	mother = models.OneToOneField(mother, on_delete=models.CASCADE)
	birth_weight = models.IntegerField(help_text="in kgs only")
	birth_defect = models.CharField(max_length=150)
	SEX_CHOICES = (
		('1', 'Male'),
		('2', 'Female'),
		('3', 'Others'),
		)
	sex = models.CharField(max_length=1, choices=SEX_CHOICES)
	#single = models.BooleanField()
	comment = models.TextField()
