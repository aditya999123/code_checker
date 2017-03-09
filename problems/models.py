from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from home.models import user_data
# Create your models here.
def validate_len(value):
    if len(value)<4:
        raise ValidationError(
            _('Problem code length cannot be smaller than 4'),
            params={'value': value},
        )
CHOICES = (
        ('PRACTICE', 'PRACTICE'),
        ('CONTEST', 'CONTEST'),
        ('LAB', 'LAB'))

class group(models.Model):
	title=models.CharField(max_length=120,null=False,blank=False)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)
	active=models.BooleanField(default=False)
	type=models.CharField(null=False,blank=False,max_length=100,choices=CHOICES,default='PRACTICE')
	def __unicode__(self):
		return self.title

class problems(models.Model):
	group=models.ForeignKey(group)
	problem_code=models.CharField(max_length=6,null=False,blank=False,validators=[validate_len],unique=True)
	title=models.CharField(max_length=100,null=False,blank=False,default="title")
	question=HTMLField()
	constraints=HTMLField()
	example=HTMLField()
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)

	class Meta:
		ordering = ('group','modified')

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

class submission(models.Model):
	problem_code=models.ForeignKey(problems)
	user=models.CharField(max_length=120,null=False,blank=False)
	code=models.TextField(max_length=12000,null=True,blank=True)
	score=models.IntegerField(null=False,blank=False,default=0)
	time=models.DecimalField(max_digits=8, decimal_places=6)
	memory=models.DecimalField(max_digits=6, decimal_places=1)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)

	def __unicode__(self):
		return self.id

class best_submission(models.Model):
	problem_code=models.ForeignKey(problems)
	submission_id=models.ForeignKey(submission)
	user=models.ForeignKey(user_data)