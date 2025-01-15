from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver

driver = webdriver.Firefox()
driver.maximize_window()
username ="standard_user"
password ="secret_sauce"
Login_url = "https://www.saucedemo.com/"
driver.get(Login_url)

username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")

username_field.send_keys(username)
password_field.send_keys(password)

Login_button= driver.find_element(By.ID, "login-button")
assert not Login_button.get_attribute("disabled")
Login_button.click()

title=driver.title
assert "Swag Labs" in title