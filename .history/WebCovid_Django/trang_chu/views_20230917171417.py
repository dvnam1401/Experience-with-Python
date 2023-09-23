from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from chromedriver_py import binary_path

# Create your views here.

options = webdriver.ChromeOptions()
options.headless = True
service = Service(executable_path=binary_path)
web_driver = webdriver.Chrome(service=service, options=options)
web_driver.get("https://vnexpress.net/chu-de/covid-19-1299")
html_page = web_driver.page_source


def index(request):
    return HttpResponse(html_page)
