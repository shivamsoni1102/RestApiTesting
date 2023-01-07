from behave import *

from Payloads.CreateBooking import BookingRequest
from Services import GlobalVariables
from Utilities.Resources import *
from Services.MakeRequest import *
from Utilities import Helper

use_step_matcher("re")


@given(
    'Update values of (?P<firstname>.+) and (?P<lastname>.+) and (?P<totalprice>.+) and (?P<depositpaid>.+) and (?P<checkin>.+) and (?P<checkout>.+) and (?P<additionalneeds>.+) params')
def step_impl(context, firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds):
    context.update_booking_request = BookingRequest(first_name=firstname, last_name=lastname,
                                                    total_price=totalprice, deposit_paid=depositpaid,
                                                    checkin=checkin, checkout=checkout,
                                                    additional_needs=additionalneeds)


@when('UpdateBooking PUT API is called')
def step_impl(context):
    context.update_booking_response = make_request(method='PUT', resource=update_booking(GlobalVariables.bookingId),
                                                   query_params=context.update_booking_request,
                                                   headers={"Accept": "application/json"},
                                                   cookies={"token": GlobalVariables.token})


@then('Booking is updated')
def step_impl(context):
    assert context.update_booking_response is not None
    assert context.update_booking_response.status_code == 200
    print(context.update_booking_response.json())
    Helper.compare_get_booking(context.update_booking_request, context.update_booking_response.json())
