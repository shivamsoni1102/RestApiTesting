from behave import *
from Payloads.CreateBooking import *
from Utilities.Resources import *
from Services.MakeRequest import *
from Utilities import Helper
from Services import GlobalVariables

use_step_matcher("re")

global bookingId


@given(
    "Pass (?P<firstname>.+) and (?P<lastname>.+) and (?P<totalprice>.+) and (?P<depositpaid>.+) and (?P<checkin>.+) and (?P<checkout>.+) and (?P<additionalneeds>.+) params")
def step_impl(context, firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds):
    context.create_booking_request = BookingRequest(first_name=firstname, last_name=lastname,
                                                    total_price=totalprice, deposit_paid=depositpaid,
                                                    checkin=checkin, checkout=checkout,
                                                    additional_needs=additionalneeds)
    GlobalVariables.create_booking_request = context.create_booking_request


@when("CreateBooking POST API is called")
def step_impl(context):
    context.create_booking_response = make_request(method='POST', resource=create_booking,
                                                   query_params=context.create_booking_request,
                                                   headers={"Accept": "application/json"})


@then("Booking is created")
def step_impl(context):
    assert context.create_booking_response is not None
    assert context.create_booking_response.status_code == 200
    print(context.create_booking_response.json())
    Helper.compare_create_booking(context.create_booking_request, context.create_booking_response.json())
    GlobalVariables.bookingId = context.create_booking_response.json()['bookingid']