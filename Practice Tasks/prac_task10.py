# As TASK number 7 we return to handle different tabs and data , Now we need collect below information from different tabs.
# Website 1 :- https://alnafi.com/courses/python
# Website 2:- https://alnafi.com/courses/sysops
# Output :-
# ['Python', 'SysOps (System Operations)']
# ['35 USD', '325 USD']

course_titles = []
price_titles = []
import csv
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://alnafi.com/courses/course/python-for-beginners")
time.sleep(5)
driver.execute_script("window.open('https://alnafi.com/courses/diploma-in-sysops-and-cloud','new window')")
wins = driver.window_handles
time.sleep(2)
driver.switch_to.window(wins[0])
print("This is my zero index "+ driver.title)
# <h1 class="banner-text-title">Python for Beginners</h1>
mycourse1 = driver.find_element(By.CLASS_NAME, "banner-text-title")
course_titles.append(mycourse1.text)
price_titles.append(0)
# myprice1 = driver.find_element(By.CLASS_NAME, "text-3xl")
# print(myprice1.text)
driver.switch_to.window(wins[1])
time.sleep(2)
print("This is my first index " + driver.title)
# <h1 class="banner-text-title !text-white">Diploma in SysOps &amp; Cloud Advancement <span class="text-white">(EduQual Level 4)</span></h1>
mycourse2 = driver.find_element(By.CLASS_NAME, "banner-text-title")
course_titles.append(mycourse2.text)
# <h1 class="text-3xl font-serif pt-4 text-BalticSea"> PKR 250,000</h1>
# //*[@id="plans"]/div/div[2]/div[4]/div/h1
myprice2 = driver.find_element(By.XPATH, "//*[@id='plans']/div/div[2]/div[4]/div/h1")
price_titles.append(myprice2.text)
time.sleep(5)
print(course_titles)
print(price_titles)

# Write data to CSV file
with open('course_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Course Title', 'Price'])
    for i in range(len(course_titles)):
        writer.writerow([course_titles[i], price_titles[i]])

driver.quit()

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender = "YOUR_EMAIL@gmail.com"
receiver = "YOUR_EMAIL@gmail.com"
app_password = "YOUR_APP_PASSWORD"

msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = receiver
msg["Subject"] = "Scraped Course Data"
msg.attach(MIMEText("Please find the course data CSV attached.", "plain"))

with open("course_data.csv", "rb") as f:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment; filename=course_data.csv")
    msg.attach(part)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, app_password)
    server.sendmail(sender, receiver, msg.as_string())

print("Email sent with CSV attachment!")
