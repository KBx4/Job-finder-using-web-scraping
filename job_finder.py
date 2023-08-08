from bs4 import BeautifulSoup  # For HTML content.
import requests                # For HTTP requests.
import time                    # For wait times.

def job_hunt(): # Scrape recent Python job listings from TimesJobs.
    
    # Fetch the webpage content.
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text #website being scraped
    soup = BeautifulSoup(html_text, 'lxml')
    # Get all job listing data from website.
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    print("Jobs for python developer posted a few days ago:")
    i = 1
    for job in jobs:
        # Extract details needed from job listing.
        company = job.find('h3', class_='joblist-comp-name').text.replace(' ', '') #variables with values provided by the webscraper
        skills = job.find('span', class_='srp-skills').text.replace(' ', '')
        fresh = job.find('span', class_='sim-posted').text
        info = job.header.h2.a['href']

        #Print only jobs listed recently.
        if 'few days ago' in fresh: # this part picks out the section with listings made in the last couple of days
            print(str(i) + ". Company name: " + company.strip())
            print("Link to job: " + info)
            print("Skills required: " + skills.strip())
            print()
            i += 1               

if __name__ == '__main__': #sequence activated if no job was found
    # Keep looking for new jobs to show.
    while True:
        job_hunt()
        time_wait = 15
        print("Waiting for 15 minutes, new jobs might come up!")
        time.sleep(time_wait*60)







