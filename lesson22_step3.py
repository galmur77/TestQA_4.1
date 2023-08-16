import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num_1 = browser.find_element(By.XPATH, '//*[@id="num1"]').text # Находим элемент с первым числом
num_1 = int(num_1)
num_2 = browser.find_element(By.XPATH, '//*[@id="num2"]').text  # аходим элемент со вторым числом
num_2 = int(num_2)
value = str(num_1 + num_2)  #
print('num_1 + num_2 =', value)  #

select = Select(browser.find_element(By.TAG_NAME, "select")) # (By.TAG_NAME, "select") или можно использовать spisok = Select(browser.find_element(By.XPATH, '//*[@id="dropdown"]')
select.select_by_visible_text(value) #  spisok.select_by_visible_text(value)

button = browser.find_element(By.XPATH, '/html/body/div/form/button') # Находим кнопку
button.click()
# закрываем браузер после всех манипуляций
time.sleep(30)
browser.quit()

