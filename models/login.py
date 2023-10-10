from selene import browser, have, be
import allure


class LoginPage:

    def __init__(self):
        self.username = browser.element('#user-name')
        self.password = browser.element('#password')

    def open_main_page(self):
        with allure.step('Открыть главную страницу'):
            browser.open('/')

    def fill_username(self, username):
        with allure.step(f'В поле Username ввести {username}'):
            self.username.click().type(username)

    def fill_password(self, password):
        with allure.step(f'В поле Password ввести {password}'):
            self.password.click().type(password)

    def click_login(self):
        with allure.step('Нажать кнопку Login'):
            browser.element('#login-button').click()

    def inventory_list_is_opened(self):
        with allure.step('Проверить, что открыта главная страница с товарами'):
            browser.element('.inventory_list').should(be.present)

    def unsunsuccessfull_login(self):
        with allure.step('Проверить, что на странице появилось сообщение с ошибкой'):
            browser.element('h3').should(have.exact_text(
                'Epic sadface: Username and password do not match any user in this service'
            ))

    def locked_user_login(self):
        with allure.step('Проверить, что появилось сообщение с ошибкой'):
            browser.element('h3').should(have.exact_text(
                'Epic sadface: Sorry, this user has been locked out.'
            ))
