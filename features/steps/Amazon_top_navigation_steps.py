from behave import when, then, given

@given('Open Amazon Search')
def open_amazon(context):
    #context.driver.get('https://www.amazon.com')
    context.app.main_page.open_main()

@when('Click Orders')
def click_orders(context):
    #context.driver.find_element(By.ID, 'nav-orders').click()
    context.app.Header.click_order()

@when('search for {search_word}')
def search_for_product(context, search_word):
    context.app.Header.input_search_word(search_word)
    context.app.Header.click_search()

@when('Move mouse over flag icon')
def hover_flag_icon(context):
    context.app.Header.hover_flag_icon()

@when('Select books department')
def select_department(context):
    context.app.Header.select_department()

@then('Spanish language selection is visible')
def verify_spanish_lang_present(context):
    context.app.Header.verify_spanish_lang_present()

@then('Verify Sign in page opened')
def verify_sign_in_opened(context):
    assert 'https://www.amazon.com/ap/signin' in context.driver.current_url

@then('Verify books department is selected')
def verify_books_department(context):
    context.app.Header.verify_books_department()