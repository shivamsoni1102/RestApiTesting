from behave import *
from Payloads.Auth import *
from Utilities.Resources import *
from Services.MakeRequest import *

use_step_matcher("re")


@given("Credentials (?P<username>.+) and (?P<password>.+) to get auth token")
def step_impl(context, username, password):
    context.auth_req_params = AuthRequest(username=username, password=password)


@when("I call CreateToken POST API method")
def step_impl(context):
    context.response = make_request(method='POST', resource=create_token,
                                    query_params=context.auth_req_params)


@then("response is 200 and token is received")
def step_impl(context):
    assert context.response is not None
    print("status code is {}".format(context.response.status_code))
    assert context.response.status_code == 200
    data = context.response.json()
    assert data["token"] is not None
    context.token = data["token"]
