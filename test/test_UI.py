from MainPage import MainPage
from DataFields import DataFild


def test_assertion(chrome_browser):
    main_page = MainPage(chrome_browser)
    main_page.find_fields()
    main_page.filling_in_the_fields()
    main_page.click_submit_button()

    data_fild = DataFild(chrome_browser)
    data_fild.find_fields()
    data_fild.get_class_userName()
    data_fild.get_class_password()
 
    assert "success" in data_fild.get_class_userName()
    assert "success" in data_fild.get_class_password()
