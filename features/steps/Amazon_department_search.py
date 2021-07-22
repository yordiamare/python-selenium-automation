from behave import when, then, given

@given('Open Amazon website')
def open_amazon(context):
    context.app.main_page.open_main()

@when('Select Amazon device')
def select_department_icon(context):
    context.app.Header.department_search()

@when ('Shop for {search_word}')
def input_search(context, search_word):
    context.app.Header.input_search_word(search_word)
    context.app.Header.click_search()

@then ('Verify Amazon device is selected')
def verify_amazon_devise(context):
    context.app.Header.verify_department()