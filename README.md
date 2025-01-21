# LinkedIn Profile Scraper for IIT Graduates
This project automates the process of logging into LinkedIn, searching for profiles of IIT graduates, scraping their information (name, job title, and company/industry), and saving the extracted data into a CSV file.

## Prerequisites
 To run this script, you will need the following:

- Python 3.x
- Google Chrome
- ChromeDriver
- Selenium library
- Installation
** Install Python 3.x: Download and install Python 3.x from the official Python website: https://www.python.org/downloads/

Install Required Libraries: You need to install the following Python libraries:

Selenium
CSV (This is a built-in library, so you don’t need to install it manually)
##  To install Selenium, run:

- bash
- Copy
- Edit
- pip install selenium
- Install ChromeDriver: Download the version of ChromeDriver that matches your Google Chrome version from: https://sites.google.com/a/chromium.org/chromedriver/

Ensure that chromedriver is available in your system's PATH, or provide the path to chromedriver in the script.

## Setup
Edit Credentials: Open the script and replace the following placeholders with your LinkedIn credentials:

USERNAME = "your email id"
PASSWORD = "your password"
Configure Output File: The output will be saved in the iit_graduates_profiles.csv file in the same directory. You can change the OUTPUT_FILE variable to a custom path if needed.

# Running the Script
After setting up the prerequisites and modifying the script, you can run it by executing the following command:

- bash
- Copy
- Edit
- python linkedin_scraper.py
The script will:

Log in to LinkedIn using the provided credentials.
Navigate to LinkedIn's search page for people with the keyword "IIT."
Scrape names, job titles, and company/industry details of IIT graduates.
Save the data in iit_graduates_profiles.csv.
## Output
The output file (iit_graduates_profiles.csv) will contain the following columns:

Name: Name of the LinkedIn profile.
Job Title: The current job title of the individual.
Company and Industry: The company and industry where the individual works.

## Error Handling
The script includes basic error handling to address the following:

- TimeoutException: Handles waiting time for elements to load.
- NoSuchElementException: Handles missing elements on the page.
- General Exception: Catches any unexpected errors and prints the message.

# Approach to Generating Insights About Career Paths for IIT Graduates
Once you have collected data on IIT graduates from LinkedIn (such as names, job titles, and companies/industries), you can use it to generate insights about their career paths. The analysis could be used to identify common trends, career progression patterns, or areas where IIT graduates are excelling. Here's an approach to analyze the data:

## Step 1: Data Cleaning and Preprocessing
Remove invalid or missing data
Standardize job titles and industries
## Step 2: Categorization
Job Title Categorization: Group similar job titles into broader categories such as:
Software Engineering (e.g., Software Engineer, Backend Developer, Full Stack Developer)
Data Science (e.g., Data Scientist, Data Analyst, Machine Learning Engineer)
## Step 3: Exploratory Data Analysis (EDA)
Job Title Analysis: Identify the most common job titles pursued by IIT graduates and examine their distribution.
Industry Analysis
Career Progression
## Step 4: Insights Generation
Top Job Categories
Industry Trends
Geographical Distribution
## Step 5: Visualization
Bar Charts and Pie Charts.
Trend Analysis
## Notes
- LinkedIn Terms of Service: Please be aware that LinkedIn has strict rules against scraping, and this script should be used with caution. Always review LinkedIn's terms of service to ensure compliance.
- LinkedIn Login: Avoid using this script for bulk or frequent scraping, as LinkedIn may block your account for suspicious activities.
- Captcha and 2FA: If LinkedIn detects automated login, you might be prompted to solve a CAPTCHA or enter a verification code.
