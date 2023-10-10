from selene import browser, have, be
import allure


class Products:

    def open_item(self, item):
        with allure.step(f'Открыть карточку "{item}"'):
            browser.all('.inventory_item_name').element_by(have.exact_text(item)).click()

    def check_item_details(self, item_details):
        with allure.step(f'Проверить, что содержимое карточки товара: "{item_details}"'):
            browser.element('.inventory_details_desc').should(have.exact_text(item_details))

    def back_to_products(self):
        with allure.step('Вернуться к товарам'):
            browser.element('#back-to-products').click()

        with allure.step('Проверить, что отрыта страница с товарами'):
            browser.element('.inventory_list').should(be.present)

    def add_item_to_cart(self, item, quantity):
        with allure.step('Добавить товар в корзину'):
            browser.element(item).click()

        with allure.step('Проверить, что количество товаров в корзине увеличилось'):
            browser.element('.shopping_cart_badge').should(be.present)
            browser.element('.shopping_cart_badge').should(have.exact_text(str(quantity + 1)))

    def open_cart(self):
        with allure.step('Перейти в корзину'):
            browser.element('.shopping_cart_link').click()

    def check_item_in_cart(self, item):
        with allure.step(f'Проверить, что товар {item} в корзине'):
            browser.element('.inventory_item_name').should(have.exact_text(item))

    def click_button(self, button_id):
        with allure.step(f'Нажать кнопку {button_id[1:].upper()}'):
            browser.element(button_id).click()

    def fill_first_name(self, first_name):
        with allure.step(f'Заполнить имя {first_name}'):
            browser.element('#first-name').click().type(first_name)

    def fill_last_name(self, last_name):
        with allure.step(f'Заполнить фамилию {last_name}'):
            browser.element('#last-name').click().type(last_name)

    def fill_zip_code(self, zip_code):
        with allure.step(f'Заполнить почтовый индекс {zip_code}'):
            browser.element('#postal-code').click().type(zip_code)

    def check_successful_order_form(self):
        with allure.step('Проверить, что заказ успешно создан'):
            browser.element('#checkout_complete_container').should(be.present)
            browser.element('.complete-header').should(have.text('Thank you for your order!'))

    def field_is_required(self, field):
        with allure.step(f'Проверить, что поле {field} обязательно для заполнения'):
            browser.element('h3').should(have.text(f'Error: {field} is required'))

    def removed_item_check(self):
        with allure.step('Проверить,что товар удален'):
            browser.element('.removed_cart_item').should(be.present)
