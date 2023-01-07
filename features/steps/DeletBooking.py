from behave import *
from Services import GlobalVariables
from Utilities.Resources import *
from Services.MakeRequest import *
from Utilities import Helper

use_step_matcher("re")


@when('DeleteBooking API is called')
def step_impl(context):
    context.delete_booking_response = make_request(method='DELETE', resource=delete_booking(GlobalVariables.bookingId),
                                                   cookies={"token": GlobalVariables.token})


@then(u'Booking is deleted')
def step_impl(context):
    print("status code - ", context.delete_booking_response.status_code)
    assert context.delete_booking_response is not None
    assert context.delete_booking_response.status_code == 201


@then('I try to call get booking api for deleted booking and verify response is 404 Not Found')
def step_impl(context):
    get_booking_response = make_request(method='GET', resource=get_booking(GlobalVariables.bookingId),
                                        headers={"Accept": "application/json"}, query_params=None)
    print("get response after booking is delete- ", get_booking_response.status_code)
    assert get_booking_response.status_code == 404


