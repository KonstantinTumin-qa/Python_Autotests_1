"""
Configuration test
"""
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://testqastudio.me/'

def test_browser(browser):
    """
    Main fixture
    """
    element = browser.find_element(by=By.CSS_SELECTOR, value='#menu-top [class*="menu-item-11088"]')
    element.click()

    assert browser.current_url == 'https://testqastudio.me/faq/', 'Unexpected url'
    
    # #page-header h1
    title = browser.find_element(by=By.CSS_SELECTOR, value='#page-header h1')
    assert title.text == 'Часто задавамые вопросы', 'Unexpected title'
    
def test_count_of_all_products(browser):
   
    """
    Test case TC-3
    """
    
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    WebDriverWait(browser, timeout=10, poll_frequency=2).until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "razzi-posts_found-inner"), "Показано 17 из 17 товары"))
         
    elements = browser.find_elements(by=By.CSS_SELECTOR, value="[id='rz-shop-content'] ul li")

    assert len(elements) == 17, "Unexpected count of products"
        
