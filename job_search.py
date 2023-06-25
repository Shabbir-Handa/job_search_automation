import time
from bs4 import BeautifulSoup
import re
import requests

# Set the time interval for each iteration
time_wait = float(input("How much time interval do you want to give for each iteration: "))

# Prompt the user to enter unfamiliar skills
print("Put some skill that you are not familiar with")
unfamiliar_skills = input(">")

# Check if unfamiliar_skills is not empty or contains only whitespace
if unfamiliar_skills != "" or unfamiliar_skills != " ":
    # Split the unfamiliar_skills by spaces, commas, or comma followed by a space
    unfamiliar_skills = re.split(" |, |,", unfamiliar_skills)
    print(f"Filtering out {unfamiliar_skills}")
else:
    # If unfamiliar_skills is empty or contains only whitespace, assign a string with multiple spaces to it
    unfamiliar_skills = '        '
    print("No skills to filter out")


def find_jobs(count):
    # Send a request to the job search website and get the HTML content
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from="
                             "submit&txtKeywords=python&txtLocation=").text
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_text, "lxml")
    # Find all the job listings
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
    for index, job in enumerate(jobs):
        # Extract the published date of the job listing
        published_date = job.find("span", class_="sim-posted").span.text
        if "few" in published_date:
            # Extract the company name, required skills, and more info URL
            company_name = job.find("h3", class_="joblist-comp-name").text.replace(" ", "")
            skills = job.find("span", class_="srp-skills").text.replace(" ", "")
            more_info = job.header.h2.a["href"]
            flag = True
            for unfamiliar_skill in unfamiliar_skills:
                # Check if any unfamiliar skill is present in the required skills
                if unfamiliar_skill.lower() in skills.lower():
                    flag = False
                    break
            if flag:
                # Create a new file and write the job details into it
                with open(f"posts/{count}_{index}.txt", "w") as f:
                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Required Skills: {skills.strip()}\n")
                    f.write(f"For More Info Refer To This URL: '{more_info}'")
                print(f"File saved: {count}_{index}.txt")


if __name__ == "__main__":
    count = 0
    while True:
        # Call the find_jobs function to search for jobs
        find_jobs(count)
        count += 1
        print(f"Waiting {time_wait} minutes")
        # Pause the execution for the specified time interval
        time.sleep(time_wait * 60)
