# Create your views here.
#coding:utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User

from forms import *
from models import *

import urllib

import sys, os

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_PATH)

import markdown
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

def brief(content, num):
	if len(content) <= num:
		return content.encode("utf-8") + "..."
	else:
		return content[:num -1].encode("utf-8") + "..."

def index(request):
	distributes = Distribute.objects.all()
	for d in distributes:
		d.content = brief(d.content, 200)
		d.read = "/read/" + urllib.quote(d.title.encode("utf-8")) + "/"
		d.delete = "/delete/" + urllib.quote(d.title.encode("utf-8")) + "/"
		d.edit = "/edit/" + urllib.quote(d.title.encode("utf-8")) + "/"
	return render_to_response("index.html", {"category" : "", "user" : request.user, "distributes" : distributes})

def read(request, title):
	title = urllib.unquote(title.encode("utf-8"))
	t = title.decode("utf-8")
	distribute = Distribute.objects.get(title = t)	
	distribute.edit = "/edit/" + urllib.quote(distribute.title.encode("utf-8")) + "/"
	distribute.delete = "/delete/" + urllib.quote(distribute.title.encode("utf-8")) + "/"
	return render_to_response("read.html", {"distribute" : distribute, "user" : request.user})

def delete(request, title):
	if request.method == "POST":
		form = FormDelete(request.POST)
		if form.is_valid():
			password = request.POST.get("password", "").strip()
			user = auth.authenticate(username = request.user.username, password = password)
			if user is not None and user.is_active:
				title = urllib.unquote(title.encode("utf-8"))
				t = title.decode("utf-8")
				try:
					distribute = Distribute.objects.get(title = t)
					distribute.delete()
				except Exception, e:
					pass
				return HttpResponseRedirect("../../")
			else:
				return render_to_response("fail.html", {"msg" : "密码错误"}, context_instance = RequestContext(request))
		else:
			return render_to_response("fail.html", {"msg" : "内容不合法"}, context_instance = RequestContext(request))
	else:
		form = FormDelete()
	return render_to_response("delete.html", {"form" : form, "user" : request.user}, context_instance = RequestContext(request))

def tech(request):
	return render_to_response("index.html", {"category" : "tech", "user" : request.user})

def proj(request):
	return render_to_response("index.html", {"category" : "proj", "user" : request.user})

def misc(request):
	return render_to_response("index.html", {"category" : "misc", "user" : request.user})

def login(request):
	if request.method == "POST":
		form = FormLogin(request.POST)
		if form.is_valid():
			username = request.POST.get("username", "").strip()
			password = request.POST.get("password", "").strip()
			user = auth.authenticate(username = username, password = password)
			if user is not None and user.is_active:
				auth.login(request, user)
				return HttpResponseRedirect("../")
			else:
				return render_to_response("fail.html", {"msg" : "用户名或密码错误"}, context_instance = RequestContext(request))
		else:
			return render_to_response("fail.html", {"msg" : "内容不合法"}, context_instance = RequestContext(request))
	else:
		form = FormLogin()
	return render_to_response("login.html", {"form" : form, "user" : request.user}, context_instance = RequestContext(request))

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect("/")

def distribute(request):
	if request.method == "POST":
		form = FormDistribute(request.POST)
		if form.is_valid():
			title = request.POST.get("title", "").strip()
			content = request.POST.get("content", "").strip()
			if len(title) and len(content):
				if not Distribute.objects.filter(title = title):
					value = request.POST.get("submit", None)
					if value == "distribute":
						content = markdown.markdown(content)
						record = Distribute(title = title, content = content)
						record.save()
					elif value == "code":
						content = highlight(content, PythonLexer(), HtmlFormatter())
						content = markdown.markdown(content)
						record = Distribute(title = title, content = content)
						record.save()
					elif value == "img":
						content = "<img src=\"" + content + "\" style=\"max-width:600px;max-height:600px;\">"
						content = markdown.markdown(content)
						record = Distribute(title = title, content = content)
						record.save()
					else:
						pass
					return HttpResponseRedirect("../")
				else:
					return render_to_response("fail.html", {"msg" : "与已有的博客标题重复"}, context_instance = RequestContext(request))
			else:
				return render_to_response("fail.html", {"msg" : "博客标题和内容不能为空"}, context_instance = RequestContext(request))
		else:
			return render_to_response("fail.html", {"msg" : "内容不合法"}, context_instance = RequestContext(request))
	else:
		form = FormDistribute()
	return render_to_response("distribute.html", {"form" : form, "user" : request.user}, context_instance = RequestContext(request))

def edit(request, title):
	if request.method == "POST":
		form = FormEdit(request.POST)
		if form.is_valid():
			title = urllib.unquote(title.encode("utf-8"))
			title = title.decode("utf-8")
			content = request.POST.get("content", "").strip()
			content = content.replace("\n", "<br>")
			content = content.replace(" ", "&nbsp;")
			if len(content):
				value = request.POST.get("submit", None)
				if value == "distribute":
					content = markdown.markdown(content)
					record = Distribute.objects.get(title = title)
					record.content += content
					record.save()
				elif value == "code":
					content = highlight(content, PythonLexer(), HtmlFormatter())
					content = markdown.markdown(content)
					record = Distribute.objects.get(title = title)
					record.content += content
					record.save()
				elif value == "img":
					content = "<img src=\"" + content + "\" style=\"max-width:600px;max-height:600px;\">"
					content = markdown.markdown(content)
					record = Distribute.objects.get(title = title)
					record.content += content
					record.save()

				else:
					pass
				return HttpResponseRedirect("")
			else:
				return render_to_response("fail.html", {"msg" : "博客内容不能为空"}, context_instance = RequestContext(request))
		else:
			return render_to_response("fail.html", {"msg" : "内容不合法"}, context_instance = RequestContext(request))
	else:
		title = urllib.unquote(title.encode("utf-8"))
		title = title.decode("utf-8")
		distribute = Distribute.objects.get(title = title)	
		distribute.delete = "/delete/" + urllib.quote(distribute.title.encode("utf-8")) + "/"
		form = FormEdit()
	return render_to_response("edit.html", {"form" : form, "user" : request.user, "distribute" : distribute}, context_instance = RequestContext(request))
