from MainPage import MainPage
from data import *

def test_assertion(chrome_browser):
    main_page = MainPage(chrome_browser)
    main_page.filling_in_the_fields('testingfechures', '553085530855308g')
    user = main_page.click_submit_button()
    assert user == 'test250995'

def test_add_game_to_cart(chrome_browser):
    main_page = MainPage(chrome_browser)
    main_page.filling_in_the_fields('testingfechures', '553085530855308g')
    user = main_page.click_submit_button()
    f_game = 'rust'
    main_page.find_game(f_game)
    game = main_page.add_to_cart()
    # очистка тестового пространства - удаление игры
    main_page.dell_from_cart()
    assert game.lower() == f_game.lower()

def test_del_game_from_cart(chrome_browser):
    main_page = MainPage(chrome_browser)
    main_page.filling_in_the_fields('testingfechures', '553085530855308g')
    user = main_page.click_submit_button()
    f_game = "No Man's Sky"
    main_page.find_game(f_game)
    main_page.add_to_cart()
    empty_cart = main_page.dell_from_cart()
    assert empty_cart == 'Ваша корзина пуста.'