from bs4 import BeautifulSoup
import requests
import urllib
from selenium import webdriver
import pandas as pd

url = 'https://www.linkedin.com/jobs/search/?currentJobId=3452610741&f_E=2&f_JT=F&f_T=9&f_TPR=r604800&geoId=103644278&keywords=software%20engineer&location=United%20States&refresh=true&sortBy=DD'

wd = webdriver.Chrome(executable_path='./chromedriver.exe')
wd.get(url)