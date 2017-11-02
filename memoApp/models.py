from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Memo(models.Model):
	title = models.CharField("Title of memo", max_length=50)
	text = models.CharField("Description of memo", max_length=200, blank=False)
	date = models.DateTimeField("date published", auto_now=True)
	def __str__(self):
		return "Title: " + self.title + " Text:" + self.text;

class Person(models.Model):
	first_name = models.CharField("First name of person",max_length=25)
	last_name = models.CharField("Last name of person",max_length=25, blank = True)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True) # validators should be a list
	def __str__(self):
		return "Name : " + self.first_name + " "+ self.last_name;

class Data(models.Model):
	name = models.CharField("Name of the attachment", max_length=50, blank=False)
	data_type = models.CharField("Type of attachement. Should actually be a list", max_length=100, blank=False)
	memo_id = models.ForeignKey(Memo, on_delete=models.CASCADE)
	def __str__(self):
		return "Name : " + self.name + "."+ self.data_type;

class MemoPerson(models.Model):
	memo_id = models.ForeignKey(Memo, on_delete=models.CASCADE)
	person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
	def __str__(self):
		return "MemoID : " + self.memo_id + " PersonID: "+ self.person_id;