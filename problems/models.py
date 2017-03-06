from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

# Create your models here.
def validate_len(value):
    if len(value)<4:
        raise ValidationError(
            _('Problem code length cannot be smaller than 4'),
            params={'value': value},
        )

class topics(models.Model):
	title=models.CharField(max_length=120,null=False,blank=False)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)
	def __unicode__(self):
		return self.title

class problems(models.Model):
	topic=models.ForeignKey(topics)
	problem_code=models.CharField(max_length=6,null=False,blank=False,validators=[validate_len])
	question=HTMLField()
	constraints=HTMLField()
	example=HTMLField()
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)
	def __unicode__(self):
		return self.problem_code

class testcase(models.Model):
	problem_code=models.ForeignKey(problems)
	input=models.TextField(max_length=12000,null=True,blank=True)
	expected_output=models.TextField(max_length=12000,null=True,blank=True)
	score=models.IntegerField(null=False,blank=False,default=0)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)

	class Meta:
		ordering = ('problem_code','score')

	def __unicode__(self):
		return str(self.problem_code)
