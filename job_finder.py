from bs4 import BeautifulSoup
import requests
import time

print("""
| IMPORTANT:
|
| If the code doesn't work, go to your terminal and use this command --->  pip install lmxl
| This will install lxml which is not installed by default in most cases
|
""")


def job_hunt(): #webscraper function using BeautifulSoup

    lang = input("""
enter your programming language of choice (example: python/html/java): """)

    html_text = requests.get(
        f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={lang}&txtLocation='
        ).text #website being scraped
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    print(f"Jobs for {lang} developer posted a few days ago:")
    i = 1
    for job in jobs:

        company = job.find('h3', class_='joblist-comp-name').text.replace(' ', '') #variables with values provided by the webscraper
        skills = job.find('span', class_='srp-skills').text.replace(' ', '')
        fresh = job.find('span', class_='sim-posted').text
        info = job.header.h2.a['href']
        if 'few days ago' in fresh: # this part picks out the section with listings made in the last couple of days
            print(str(i) + ". Company name: " + company.strip())
            print("Link to job: " + info)
            print("Skills required: " + skills.strip())
            print()
            i += 1
    print("""
    That's all for now!
    """)       
    time.sleep(3)        

    if __name__ == '__main__': #sequence activated if no job was found
        print("""
        [1] Search in 15 minutes
        [2] Search immediately
        [3] End search
        """)

        nojob_choice = input("How would You like to proceed: ")

        if nojob_choice == "1":
            while True:
                job_hunt()
                time_wait = 15
                print("Waiting for 15 minutes, new jobs might come up!")
                time.sleep(time_wait*60)
        elif nojob_choice == "2":
            job_hunt()
        elif nojob_choice == "3":
            print("Good Luck!")
        else:
            print("Invalid input")

job_hunt()









