import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_the_guest_should_see_a_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    try:
        browser.find_element_by_css_selector(".btn-add-to-basket")
        print("Кнопка ''Добавить в корзину'' присутствует!")
    except NoSuchButtonError:
        print("Кнопка ''Добавить в корзину'' отсутствует!")
        

    
    
    """
    Если необходимо проверить наличие текста у кнопки:
    
    button_text_elt = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    assert button_text_elt > 0, "Текст у кнопки "Добавить в корзину" отсутствует!"
    """
    
    
    """
    Если необходимом проверить правильное наименование кнопки:
    
    # находим элемент, содержащий кнопку с текстом "Добавить в корзину"
    button_text_elt = browser.find_element_by_css_selector(".btn-add-to-basket")
    # записываем в переменную button_text текст из элемента button_text_elt
    button_text = button_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Добавить в корзину!" == button_text, "Кнопка с текстом "Добавить в корзину" присутствует!"
    """
    
    
    