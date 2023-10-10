import allure
from allure_commons.types import Severity
from models.products import Products
from data.user import User

pytestmark = [
    allure.label('layer', 'web'),
    allure.label('owner', 'ytamonova'),
    allure.tag('web')
]

existing_user = User('Natalia', 'Petrova', 'standard_user', 'secret_sauce', '000000')


@allure.title('Open item card')
@allure.severity(Severity.NORMAL)
def test_open_item(login):
    products = Products()

    products.open_item('Sauce Labs Bike Light')
    products.check_item_details(
        'A red light isn\'t the desired state in testing '
        'but it sure helps when riding your bike at night. '
        'Water-resistant with 3 lighting modes, 1 AAA battery included.'
    )
    products.back_to_products()


@allure.title('Successfull order')
@allure.severity(Severity.CRITICAL)
def test_successfull_order(login):
    quantity = 0
    products = Products()

    products.add_item_to_cart('#add-to-cart-sauce-labs-fleece-jacket', quantity)
    products.open_cart()
    products.check_item_in_cart('Sauce Labs Fleece Jacket')
    products.click_button('#checkout')
    products.fill_first_name(existing_user.first_name)
    products.fill_last_name(existing_user.last_name)
    products.fill_zip_code(existing_user.zip_code)
    products.click_button('#continue')
    products.check_item_in_cart('Sauce Labs Fleece Jacket')
    products.click_button('#finish')
    products.check_successful_order_form()
    products.back_to_products()


@allure.title('Required data check')
@allure.severity(Severity.BLOCKER)
def test_required_data(login):
    quantity = 0
    products = Products()

    products.add_item_to_cart('#add-to-cart-sauce-labs-fleece-jacket', quantity)
    products.open_cart()
    products.check_item_in_cart('Sauce Labs Fleece Jacket')
    products.click_button('#checkout')
    products.click_button('#continue')
    products.field_is_required('First Name')
    products.fill_first_name(existing_user.first_name)
    products.click_button('#continue')
    products.field_is_required('Last Name')
    products.fill_last_name(existing_user.last_name)
    products.click_button('#continue')
    products.field_is_required('Postal Code')
    products.click_button('#cancel')


@allure.title('Remove item')
@allure.severity(Severity.CRITICAL)
def test_remove_item(login):
    quantity = 0
    products = Products()

    products.add_item_to_cart('#add-to-cart-sauce-labs-fleece-jacket', quantity)
    products.open_cart()
    products.click_button('#remove-sauce-labs-fleece-jacket')
    products.removed_item_check()
