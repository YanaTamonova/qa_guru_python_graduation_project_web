import allure
from allure_commons.types import Severity
from data.user import User
from models.login import LoginPage

pytestmark = [
    allure.label('layer', 'UI test'),
    allure.label('owner', 'ytamonova'),
    allure.tag('web'),
    allure.tag('login')
]

existing_user = User('Natalia', 'Petrova', 'standard_user', 'secret_sauce', '000000')
non_existing_user = User('Dmitry', 'Lomov', 'user', 'user', '000001')
locked_user = User('Svetlana', 'Mitina', 'locked_out_user', 'secret_sauce', '000002')


@allure.title('Successfull login')
@allure.severity(Severity.CRITICAL)
def test_successfull_login():
    login_page = LoginPage()

    login_page.open_main_page()
    login_page.fill_username(existing_user.username)
    login_page.fill_password(existing_user.password)
    login_page.click_login()
    login_page.inventory_list_is_opened()


@allure.title('Non existing user login')
@allure.severity(Severity.BLOCKER)
def test_non_existing_user_login():
    login_page = LoginPage()

    login_page.open_main_page()
    login_page.fill_username(non_existing_user.username)
    login_page.fill_password(non_existing_user.password)
    login_page.click_login()
    login_page.unsunsuccessfull_login()


@allure.title('Locked user login')
@allure.severity(Severity.BLOCKER)
def test_locked_user_login():
    login_page = LoginPage()

    login_page.open_main_page()
    login_page.fill_username(locked_user.username)
    login_page.fill_password(locked_user.password)
    login_page.click_login()
    login_page.locked_user_login()
