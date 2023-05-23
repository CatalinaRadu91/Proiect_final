from browser import Browser
from pages.account_page import AccountPage
from pages.cart_page import CartPage
from pages.forgot_password_page import ForgotPassword
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.products_page import ProductPage


def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.login_page = LoginPage()
    context.account_page = AccountPage()
    context.cart_page = CartPage
    context.products_page = ProductPage()
    context.forgot_password_page = ForgotPassword()


def after_scenario(context, feature):
    context.browser.clear_cache()
