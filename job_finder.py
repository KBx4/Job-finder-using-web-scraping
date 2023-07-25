from bs4 import BeautifulSoup
import requests
import time

def job_hunt():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    print("Jobs for python developer posted a few days ago:")
    i = 1
    for job in jobs:

        company = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_='srp-skills').text.replace(' ', '')
        fresh = job.find('span', class_='sim-posted').text
        info = job.header.h2.a['href']
        if 'few days ago' in fresh:
            print(str(i) + ". Company name: " + company.strip())
            print("Link to job: " + info)
            print("Skills required: " + skills.strip())
            print()
            i += 1

if __name__ == '__main__':
    while True:
        job_hunt()
        time_wait = 15
        print("Waiting for 15 minutes, new jobs might come up!")
        time.sleep(time_wait*60)







