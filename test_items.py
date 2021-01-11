import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_page_has_add_to_basket_locale(browser):
    browser.get(link)
    #time.sleep(30)
    has_button = browser.find_element_by_class_name('btn-add-to-basket')
    assert has_button, 'кнопка добавления в корзину отсутствует'
    
