from .Pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"
def test_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()


# def test_guest_can_go_to_login_page(browser):
#    browser.get(link)
#    go_to_login_page(browser)

