import pytest
#import time
from selenium import webdriver

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_btn_add_to_basket(browser, link):
    browser.get(link)
    try:
        element_btnAddToBasket = browser.find_element_by_class_name("btn-add-to-basket")
        btnAddToBasket = True
    except:
        btnAddToBasket = False
    assert btnAddToBasket == True, "Element button not found"        
