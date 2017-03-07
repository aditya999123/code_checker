from __future__ import unicode_literals

from django.db import models

# Create your models here.

class KEYS_List(models.Model):
	key=models.CharField(max_length=1200,null=False,blank=False)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)
	def __unicode__(self):
		return self.key

class KEYS_internal(models.Model):
	key=models.ForeignKey(KEYS_List)
	value=models.CharField(max_length=1200,null=True,blank=True)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)

class KEYS_external(models.Model):
	key=models.ForeignKey(KEYS_List)
	value=models.CharField(max_length=1200,null=True,blank=True)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)
