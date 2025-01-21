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
##T o install Selenium, run:

-bash
-Copy
-Edit
-pip install selenium
-Install ChromeDriver: Download the version of ChromeDriver that matches your Google Chrome version from: https://sites.google.com/a/chromium.org/chromedriver/

Ensure that chromedriver is available in your system's PATH, or provide the path to chromedriver in the script.

#Setup
Edit Credentials: Open the script and replace the following placeholders with your LinkedIn credentials:

USERNAME = "your email id"
PASSWORD = "your password"
Configure Output File: The output will be saved in the iit_graduates_profiles.csv file in the same directory. You can change the OUTPUT_FILE variable to a custom path if needed.

#Running the Script
After setting up the prerequisites and modifying the script, you can run it by executing the following command:

bash
Copy
Edit
python linkedin_scraper.py
The script will:

Log in to LinkedIn using the provided credentials.
Navigate to LinkedIn's search page for people with the keyword "IIT."
Scrape names, job titles, and company/industry details of IIT graduates.
Save the data in iit_graduates_profiles.csv.
##Output
The output file (iit_graduates_profiles.csv) will contain the following columns:

Name: Name of the LinkedIn profile.
Job Title: The current job title of the individual.
Company and Industry: The company and industry where the individual works.
##Error Handling
The script includes basic error handling to address the following:

TimeoutException: Handles waiting time for elements to load.
NoSuchElementException: Handles missing elements on the page.
General Exception: Catches any unexpected errors and prints the message.
#Notes
LinkedIn Terms of Service: Please be aware that LinkedIn has strict rules against scraping, and this script should be used with caution. Always review LinkedIn's terms of service to ensure compliance.
LinkedIn Login: Avoid using this script for bulk or frequent scraping, as LinkedIn may block your account for suspicious activities.
Captcha and 2FA: If LinkedIn detects automated login, you might be prompted to solve a CAPTCHA or enter a verification code.
