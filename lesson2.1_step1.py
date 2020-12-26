from selenium import webdriver
import math
import time

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    def calc(x):
    	return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input1 =  browser.find_element_by_id('answer')
    input1.send_keys(y)


    #Отметить checkbox "I'm the robot".

    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()

    #Выбрать radiobutton "Robots rule!".

    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()

#Нажать на кнопку Submit.

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    
    time.sleep(10)
    browser.quit()