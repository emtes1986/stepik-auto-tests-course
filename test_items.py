import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_basket_link_on_page(browser):
    browser.get(link)
    time.sleep(30) 
    basket = browser.find_element_by_css_selector(".basket-mini .btn-group > a")
    assert basket, "кнопка не найдена"
