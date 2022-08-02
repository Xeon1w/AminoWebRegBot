import time
import secmail
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
mail = secmail.SecMail()


def threadit():
    email = generate_email()
    driver.get("https://aminoapps.com")
    driver.find_element(by=By.XPATH, value="/html/body/header/div/div/nav/ul/li[3]/a").click()
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/div/div[2]/div[2]/button").click()
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/div/div[4]/div[4]/div[2]/button[2]").click()
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/div/div[4]/form[1]/div[1]/input").send_keys(
        Keys.NUMPAD0,
        Keys.NUMPAD3,
        Keys.NUMPAD0,
        Keys.NUMPAD5,
        Keys.NUMPAD2,
        Keys.NUMPAD0,
        Keys.NUMPAD0,
        Keys.NUMPAD0)
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/div/div[4]/form[1]/div[2]/button").click()
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/div/div[4]/form[3]/input").send_keys(
        "{}".format(email))
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/div/div[4]/form[3]/div/button").click()
    time.sleep(3)
    get_code(email)
    code = input("WRITE CODE >>> ")
    for i in code[0]:
        if i == 0:
            code = "0" + code
    code = int(code)
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/div/div[4]/div[6]/div[1]/input[1]").send_keys(code)
    time.sleep(3)
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/div/div[4]/div[7]/input").send_keys("rm4Fkemi")
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/div/div[4]/div[7]/div[1]/button[2]").click()
    time.sleep(1)
    try:
        driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/div/div[4]/div[8]/div[1]/img[1]").click()
    except:
        input("ENTER...")
    input("DOWNLAND PHOTO...")
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/div/div[4]/div[8]/div[2]/input").send_keys("testBot")
    try:
        driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/div/div[4]/div[8]/div[3]/label/text()[1]").click()
    except: input("PRESS TO BUTTON AND USE ENTER...")
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/div/div[4]/div[8]/div[4]/button[2]").click()
    time.sleep(8)
    with open("accounts.txt", "a")as file:
        file.write(f"{email} rm4Fkemi\n")
    driver.find_element(by=By.XPATH, value="/html/body/header/div/div/nav/ul/li[3]/a/img").click()
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="/html/body/header/div/div/nav/ul/li[3]/a/div/div/div/section[1]/label/a").click()


def generate_email():
    email = mail.generate_email()
    return email


def get_code(email):
    try:
        print("email: {}".format(email))
        messageidcheak = mail.get_messages(email).id[0]
        messagelink = mail.read_message(email, messageidcheak).htmlBody
        bs = BeautifulSoup(messagelink, "lxml")
        webbrowser.open_new(str(bs.find_all('a')[0]['href']))
    except IndexError:
        print("CHECK EMAIL...")
        print("CAPTCHA...")
        input("PRESS ENTER...")
        time.sleep(7)
        get_code(email)


def main():
    threadit()


if __name__ == '__main__':
    main()
