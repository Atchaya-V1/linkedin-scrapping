import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# LinkedIn credentials
USERNAME = "your email id"
PASSWORD = "your password"

OUTPUT_FILE = "iit_graduates_profiles.csv"

# Function to log into LinkedIn
def login_to_linkedin(driver):
    driver.get("https://www.linkedin.com/login")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    print("Logged into LinkedIn successfully.")

# Function to scrape LinkedIn profiles
def scrape_profiles(driver):
    profiles = []

    driver.get("https://www.linkedin.com/search/results/people/?keywords=IIT")
    time.sleep(5)  # Allow the page to load

    # Scroll to load multiple profiles
    for _ in range(3):  
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
    profile_sections = driver.find_elements(By.CLASS_NAME, "entity-result__content")
    for section in profile_sections:
        try:
            name = section.find_element(By.CLASS_NAME, "entity-result__title-text").text.strip()
            job_title = section.find_element(By.CLASS_NAME, "entity-result__primary-subtitle").text.strip()
            company_and_industry = section.find_element(By.CLASS_NAME, "entity-result__secondary-subtitle").text.strip()
            
            profiles.append({
                "Name": name,
                "Job Title": job_title,
                "Company and Industry": company_and_industry,
            })
        except NoSuchElementException:
            continue

    return profiles

# Function to save data to CSV
def save_to_csv(data, output_file):
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Job Title", "Company and Industry"])
        writer.writeheader()
        writer.writerows(data)
    print(f"Data successfully saved to {output_file}")

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    try:
        login_to_linkedin(driver)
        time.sleep(5)  
        profiles = scrape_profiles(driver)
        save_to_csv(profiles, OUTPUT_FILE)

    except TimeoutException:
        print("Timeout while waiting for elements to load.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    main()
