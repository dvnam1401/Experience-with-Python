from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# Create your views here.

def index(request):
    return HttpResponse("Xin chao, day la trang chu")
