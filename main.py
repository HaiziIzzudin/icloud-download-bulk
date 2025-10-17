from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import math
from time import sleep

# Automatically downloads and manages GeckoDriver
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("INSERT LINK DIRECT TO PHOTOS HERE")
print(driver.title)
# driver.quit()



def move_cursor_in_circle(driver, radius=100, steps=36, delay=0.05):
    size = driver.get_window_size()
    width, height = size["width"], size["height"]

    center_x = width // 2
    center_y = height // 2

    actions = ActionChains(driver)
    actions.move_by_offset(center_x, center_y).perform()  # start from center
    x0, y0 = center_x, center_y

    for i in range(steps + 1):
        angle = 2 * math.pi * i / steps
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)

        # only move if inside viewport
        if 0 <= x <= width and 0 <= y <= height:
            actions.move_by_offset(x - x0, y - y0).perform()
            x0, y0 = x, y
            # time.sleep(delay)


while True:
    download_btn = '//*[@id="View72"]'
    next_btn = '//*[@id="View77"]'

    # move_cursor_in_circle(driver)
    e = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, download_btn)))
    if e:    e.click()

    sleep(1)

    e = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, next_btn)))

    e.send_keys(Keys.ARROW_RIGHT)

    sleep(1)
