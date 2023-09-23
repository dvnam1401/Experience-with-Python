from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from chromedriver_py import binary_path

# Create your views here.

options = Options()
options.headless = True
web_driver = webdriver.Chrome(executable_path=binary_path, options=options)
web_driver.get("https://vnexpress.net/chu-de/covid-19-1299")
html_page = web_driver.page_source
def index(request):
    return HttpResponse(html_page)
