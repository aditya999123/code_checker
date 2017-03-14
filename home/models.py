from __future__ import unicode_literals

from django.db import models
import hashlib
# Create your models here.

class KEYS_List(models.Model):
	key=models.CharField(max_length=1200,null=False,blank=False,unique=True)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)
	def __unicode__(self):
		return str(self.key)

class KEYS_internal(models.Model):
	key=models.ForeignKey(KEYS_List,to_field='key')
	value=models.CharField(max_length=1200,null=True,blank=True)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)

CHOICES = (
        ('ADMIN', 'ADMIN'),
        ('USER', 'USER'))

class user_data(models.Model):
	username=models.CharField(max_length=100,null=False,blank=False)
	type=models.CharField(max_length=100,null=False,blank=False,default='USER')

	class Meta:
		ordering = ('type',)

	def __unicode__(self):
		return self.username