from behave import *


@given('home: I am a user on zonia.ro home page, I click on Contul meu and then I click login')
def step_impl(context):
    context.home_page.navigate_to_home_page()
    context.home_page.click_accept_notification_btn()
    context.home_page.click_contul_meu_btn()
    context.home_page.click_login_btn()


@given('home: I am a user on zonia.ro home page')
def step_impl(context):
    context.home_page.navigate_to_home_page()


@when('home: I search after "Rochie Madeira Rosie"')
def step_impl(context):
    context.home_page.search_after("Rochie Madeira Rosie")


@when('home: I search after {query}')
def step_impl(context, query):
    context.home_page.search_after(query)


@when('home: I click on {tab_name}')
def step_impl(context, tab_name):
    context.home_page.click_on_menu_tab(tab_name)
