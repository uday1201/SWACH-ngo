from djongo import models
from django.utils import timezone
from datetime import datetime


def audioFilesPath(instance, filename):
    return 'Static/Uploads/Audio_Files/' + instance.audioFor + '/' + filename

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
	lmp = models.DateField('lmp')
	baby_delivered = models.BooleanField()

	'''def _stage_cal(lmp, baby_delivered):
		date_format = "%Y/%m/%d"
		a = datetime.strptime(str(datetime.now().date()), date_format)
		#date_format2 = "%Y/%m/%d"
		b = datetime.strptime(str(lmp), date_format)
		delta = b - a
		diff = delta.days
		if baby_delivered==False:
			if diff<=98:
				stage = 'first'
			elif 98<diff<=196:
				stage = 'second'
			else :
				stage = 'third'
		elif baby_delivered==True:
			if diff<=322:
				stage = 'fourth'
			elif 322<diff<=460:
				stage = 'fifth'
			elif 460<diff<=645:
				stage = 'sixth'
			elif 645<diff<=1010:
				stage = 'seventh'
		return stage

	stage = models.CharField(_stage_cal(lmp, baby_delivered) ,editable=False)'''

	husband_name = models.CharField(max_length=150)
	district = models.ForeignKey(district, on_delete=models.SET_NULL, null=True)
	chc = models.ForeignKey(chc, on_delete=models.SET_NULL, null=True)
	village = models.ForeignKey(village, on_delete=models.SET_NULL, null=True)
	phc = models.ForeignKey(phc, on_delete=models.SET_NULL, null=True)
	asha_name = models.ForeignKey(asha, on_delete=models.SET_NULL, null=True)
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

class stage(models.Model):
	STAGES = (
		('1', 'first'),
		('2', 'second'),
		('3', 'third'),
		('4', 'fourth'),
		('5', 'fifth'),
		('6', 'sixth'),
		('7', 'seventh'),
		)
	stage = models.CharField(max_length=1, choices=STAGES) 

	def __str__(self):
		return self.stage


class Attachment(models.Model):
	file = models.FileField(upload_to = 'attachments')

class audio(models.Model):
	stage = models.ForeignKey(stage, on_delete=models.CASCADE)
	audio = models.ManyToManyField(Attachment)