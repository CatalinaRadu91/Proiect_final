from behave import *



@then('{page_name}: I verify that the url is "https://www.emag.ro/{url_path}"')
def step_impl(context, url_path, page_name):
    assert context.browser.driver.current_url == "https://www.emag.ro/" + url_path