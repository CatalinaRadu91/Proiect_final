from behave import *


@when('products: I click on product name "Rochie Madeira Rosie"')
def step_impl(context):
    context.products_page.select_product_by_name("Rochie Madeira Rosie")


@when('products: I select size for the product and I add it to basket')
def step_impl(context):
    context.products_page.select_size_S()
    context.products_page.add_product_to_basket()


@when('products: I click on Cosul meu button')
def step_impl(context):
    context.products_page.click_cart_btn()


@then('products: I verify that results contain search query {query}')
def step_impl(context, query):
    context.products_page.verify_results_contains_text(query)