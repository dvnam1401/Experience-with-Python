from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from chromedriver_py import binary_path

# Create your views here.

options = Options()
options.headless = True
web_driver = webdriver.Chrome(executable_pat=binary_path, options=options)
web_driver.get()
def index(request):
    return HttpResponse("Xin chao, day la trang chu")
