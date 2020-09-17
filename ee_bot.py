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
        (By.XPATH, '/html/body/div[1]/div/main/div/div/div/div/div/div/div[1]/div/a/div[1]/div[2]')))
    # /html/body/div[1]/div/main/div/div/div/div/div/div/div[1]/div/a/div[1]/div[2]
    # /html/body/div[1]/div/main/div/div/div/div/div/div/div[1]/div/a/div[1]/div[2]
    # /html/body/div[1]/div/main/div/div/div/div/div/div/div[1]/div/a/div[1]/div[1]/img
    # /html/body/div[1]/div/main/div/div/div/div/div/div/div[1]/div/a/div[1]/div/img
    item.click()

    size = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[1]/div/main/div[1]/div/div/div/div/div[2]/div/form/div[1]/fieldset/div[5]')))
    size.click()

    # clicks add to cart
    add_to_cart = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[1]/div/main/div[1]/div/div/div/div/div[2]/div/form/button')))
    add_to_cart.click()

    checkout = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[2]/div/form/div[2]/button')))
    checkout.click()

    # shop_pay = wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, '/html/body/div[1]/div/div/header/div/div[1]/div/div[2]/div/div[2]/div/div/div[1]/div')))
    # shop_pay.click()

    # email = wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, '/html/body/div/section/div[1]/div[1]/div/div[1]/form/section/div/div[2]/div/input')))
    # email.send_keys(k["email"])

    email = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[1]/div/div/main/div[1]/form/div[1]/div[1]/div[2]/div[1]/div/div/input')))
    email.send_keys(k["email"])

    f_name = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[1]/input')))
    f_name.send_keys(k["f_name"])

    l_name = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[1]/input')))
    l_name.send_keys(k["l_name"])

    address = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[4]/div[1]/input')))
    address.send_keys(k["address"])

    city = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[5]/div[1]/input')))
    city.send_keys(k["zip"])

    state = Select(driver.find_element_by_xpath(
        '/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/div[1]/div[3]/div[1]/select[1]'))
    state.select_by_visible_text(k["state"])

    zip_code = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[5]/div[1]/input')))
    zip_code.send_keys(k["zip"])

    phone = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[5]/div[1]/input')))
    phone.send_keys(k["zip"])


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.ericemanuel.com/collections/shortest')
    order(keys)
    #schedule.every().thursday.at("11:00").do(order, keys)

    while True:
        schedule.run_pending()
        time.sleep(1)
