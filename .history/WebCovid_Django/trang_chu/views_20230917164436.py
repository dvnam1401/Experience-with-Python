from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from chromedriver_py import binary_path

# Create your views here.

def index(request):
    return HttpResponse("Xin chao, day la trang chu")
