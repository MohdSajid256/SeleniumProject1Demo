from selenium import webdriver


driver = webdriver.Chrome()

driver.get("http://selenium.dev")
title = driver.title
driver.fullscreen_window()
print(title)
assert "Selenium" in title

