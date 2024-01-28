import time
import pandas as pd
from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://rpachallenge.com')
time.sleep(1)

start_button = driver.find_element(By.XPATH, '//button[text()="Start"]')
start_button.click()


def excel():
    list_of_lists = []
    df = pd.read_excel('challenge (1).xlsx', engine='openpyxl')

    for x in range(len(df.index)):
        list_of_lists.append(list(df.loc[x]))

    for each in list_of_lists:
        try_here(each[0], each[1], each[2], each[3], each[4], each[5], each[6], driver)


def try_here(first_name, last_name, company, job, address, mail, phone, driver_html):

    sibling_input_first_name = driver_html.find_element(By.XPATH, '//label[text()="First Name"]/following-sibling::input')
    sibling_input_first_name.send_keys(first_name)

    sibling_input_last_name = driver_html.find_element(By.XPATH, '//label[text()="Last Name"]/following-sibling::input')
    sibling_input_last_name.send_keys(last_name)

    sibling_input_company = driver_html.find_element(By.XPATH, '//label[text()="Company Name"]/following-sibling::input')
    sibling_input_company.send_keys(company)

    sibling_input_job = driver_html.find_element(By.XPATH, '//label[text()="Role in Company"]/following-sibling::input')
    sibling_input_job.send_keys(job)

    sibling_input_address = driver_html.find_element(By.XPATH, '//label[text()="Address"]/following-sibling::input')
    sibling_input_address.send_keys(address)

    sibling_input_phone = driver_html.find_element(By.XPATH, '//label[text()="Phone Number"]/following-sibling::input')
    sibling_input_phone.send_keys(str(phone))

    sibling_input_mail = driver_html.find_element(By.XPATH, '//label[text()="Email"]/following-sibling::input')
    sibling_input_mail.send_keys(mail)

    submit_button = driver_html.find_element(By.XPATH, '//input[@value="Submit"]')
    submit_button.click()


excel()

time.sleep(3)
driver.quit()

