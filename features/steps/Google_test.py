from behave import given

@given('Open Google')
def Open_Google(context):
    context.app.main_page.open_other_url()

