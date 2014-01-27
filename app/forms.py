#coding:utf-8

from django import forms
from django.forms import ModelForm 

from app.models import *

class FormLogin(ModelForm):
	username = forms.CharField(max_length = 10, widget = forms.TextInput(attrs = {"class" : "form-control", "placeholder" : "用户名"}))
	password = forms.CharField(max_length = 20, widget = forms.PasswordInput(attrs = {"class" : "form-control", "placeholder" : "密码"}))
	
	class Meta:
		model = Administrator
		fields = ["username", "password"]

class FormDistribute(ModelForm):
	title = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {"class" : "form-control", "placeholder" : "标题"}))
	content = forms.CharField(max_length = 65536, widget = forms.Textarea(attrs = {"class" : "form-control", "rows" : "15"}))

	class Meta:
		model = Distribute
		fields = ["title", "content"]

class FormDelete(forms.Form):
	password = forms.CharField(max_length = 20, widget = forms.PasswordInput(attrs = {"class" : "form-control", "placeholder" : "密码"}))

class FormEdit(forms.Form):
	content = forms.CharField(max_length = 65536, widget = forms.Textarea(attrs = {"class" : "form-control", "rows" : "15"}))
