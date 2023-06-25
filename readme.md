# Job Search Automation

This Python script automates the process of job searching on the website TimesJobs (https://www.timesjobs.com/). It allows you to filter out job listings based on unfamiliar skills and saves the details of relevant jobs into separate text files.


## Getting Started

To use this script, follow the instructions below:

1. Clone the repository by running the following command in your terminal or command prompt:

```
git clone <repository_url>
```

2. Navigate to the project directory:

```
cd job-search-automation
```

3. Open the file `job_search.py` in a text editor.

4. Customize the script by modifying the variables as per your requirements (refer to the "Customization" section in the README).

5. Save the changes and close the file.

## Prerequisites

Before running the script, ensure that you have the following dependencies installed:

- Python 3.x
- Beautiful Soup (bs4)
- Requests

You can install the required packages by running the following command:

```
pip install -r requirements.txt
```
## How to Use

1. Open a terminal or command prompt and navigate to the project directory.

2. Run the script using the following command:

```
python job_search.py
```

3. You will be prompted to enter the time interval (in minutes) for each iteration. Enter the desired value and press Enter.

4. Next, you will be asked to input any unfamiliar skills that you want to filter out from the job listings. Enter the skills separated by spaces, commas, or comma followed by a space.

5. The script will continuously search for job listings on TimesJobs and save the relevant details into separate text files. The files will be stored in the `posts` directory.

6. To stop the script, press `Ctrl+C` in the terminal or command prompt.

## Customization

You can customize the script according to your needs by modifying the following variables:

- `time_wait`: Set the time interval (in minutes) between each iteration. By default, it prompts the user for input.

- `unfamiliar_skills`: Specify any unfamiliar skills that you want to filter out from the job listings. By default, it prompts the user for input.

- `html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from="
                             "submit&txtKeywords=python&txtLocation=").text`: Change the URL to modify the job search criteria. The default URL searches for jobs with the keyword "python" and no specific location.

- `with open(f"posts/{count}_{index}.txt", "w") as f`: Modify the file path and format to change the saved file structure. By default, it saves files with names like "0_0.txt", "0_1.txt", etc., in the `posts` directory.

## Disclaimer

This script is provided as-is and serves as a starting point for automating job searches. Use it responsibly and in accordance with the terms and conditions of the target website. The script may require adjustments if the target website's structure or layout changes.

**Note:** This script was last updated in June 2023.