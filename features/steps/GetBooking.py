from behave import *

from Services import GlobalVariables
from Utilities.Resources import *
from Services.MakeRequest import *
from Utilities import Helper

use_step_matcher("re")


@given("Pass booking id")
def step_impl(context):
    print("booking is ", str(GlobalVariables.bookingId))


@when("GetBooking API is called")
def step_impl(context):
    context.get_booking_response = make_request(method='GET', resource=get_booking(GlobalVariables.bookingId),
                                                headers={"Accept": "application/json"}, query_params=None)


@then("Booking is returned")
def step_impl(context):
    print("status code - ", context.get_booking_response.status_code)
    assert context.get_booking_response is not None
    assert context.get_booking_response.status_code == 200
    Helper.compare_get_booking(GlobalVariables.create_booking_request, context.get_booking_response.json())
