from bs4 import BeautifulSoup
import requests


html_text = requests.get('https://uk.indeed.com/jobs?q=python&l=United+Kingdom').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.findAll('td', class_="resultContent")
#job_title = jobs.findAll('h2class_="jobTitle jobTitle-color-purple").text.replace(' ', '')
#print(job_title)
print(jobs)