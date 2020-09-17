from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import schedule
import time
from supreme_config import keys
from timeme import timeme


@timeme
def order(k):

    wait = WebDriverWait(driver, 10)

    # clicks on the item you want to purchase
    item = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[2]/ul/li[3]/div/a/img')))
    item.click()

    # sleep for a second to allow the sizes to appear clickable
    time.sleep(1)

    # selects a size
    size = Select(driver.find_element_by_xpath(
        '/html/body/div[2]/div/div[2]/div/form/fieldset[1]/select'))
    size.select_by_visible_text(k["size"])

    # clicks add to cart
    add_to_cart = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[2]/div/div[2]/div/form/fieldset[2]/input')))
    add_to_cart.click()

    # clicks checkout
    checkout = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[2]/div/div[1]/div/a[2]')))
    checkout.click()

    # types in the name
    name = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[1]/input')))
    name.send_keys(k["name"])

    # types in the email
    email = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[2]/input')))
    email.send_keys(k["email"])

    # types in the phone number
    tel = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[3]/input')))
    tel.send_keys(k["phone"])

    # types in the address
    address = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[4]/div[1]/input')))
    address.send_keys(k["address"])

    # types in the zip code
    zip_code = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[5]/div[1]/input')))
    zip_code.send_keys(k["zip"])

    # enters the card number
    card_number = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/div[1]/div[2]/input')))
    for x in k["card_number"]:
        card_number.send_keys(x)

    # enters the expiring month
    month = Select(driver.find_element_by_xpath(
        '/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/div[1]/div[3]/div[1]/select[1]'))
    month.select_by_visible_text(k["month"])

    # enters the expiring year
    year = Select(driver.find_element_by_xpath(
        '/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/div[1]/div[3]/div[1]/select[2]'))
    year.select_by_visible_text(k["year"])

    # enters the cvv code
    cvv = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/div[1]/div[3]/div[2]/input')))
    cvv.send_keys(k["cvv"])

    # clicks on the terms and condidtions box
    driver.find_element_by_xpath(
        '//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()

    # clicks on process payment
    driver.find_element_by_xpath(
        '/html/body/div[2]/div[1]/form/div[3]/div[2]/input').click()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.supremenewyork.com/shop/all')
    order(keys)
    #schedule.every().thursday.at("11:00").do(order, keys)

    while True:
        schedule.run_pending()
        time.sleep(1)
