from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)                           # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                                                 # открываю страницу
    page.click_btn_add_to_basket()                              # выполняю метод страницы — добавляю товар в корзину
    page.solve_quiz_and_get_code()
    page.product_name_should_be_equal_in_basket()               # проверяю совпадают ли имена товара отправленного в корзину с именем добавляемого товара
    page.total_price_should_be_equal_product_price()            # сравниваю цену товара с ценой корзины

