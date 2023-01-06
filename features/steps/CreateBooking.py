from behave import *
from Payloads.CreateBooking import *
from Utilities.Resources import *
from Services.MakeRequest import *

use_step_matcher("re")


@given(
    "Pass (?P<firstname>.+) and (?P<lastname>.+) and (?P<totalprice>.+) and (?P<depositpaid>.+) and (?P<checkin>.+) and (?P<checkout>.+) and (?P<additionalneeds>.+) params")
def step_impl(context, firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds):
    print("firstname is " + firstname)
    context.request_body = BookingRequest(first_name=firstname, last_name=lastname,
                                          total_price=totalprice, deposit_paid=depositpaid,
                                          checkin=checkin, checkout=checkout,
                                          additional_needs=additionalneeds)


@when("CreateBooking POST API is called")
def step_impl(context):
    context.response = make_request(method='POST', resource=create_booking,
                                    query_params=context.request_body, headers={"Accept": "application/json"})


@then("Booking is created")
def step_impl(context):
    assert context.response is not None
    response = context.response.json()
    request = context.request_body
    print("status code is {}".format(context.response.status_code))
    assert context.response.status_code == 200
    assert response["bookingid"] is not None
    context.booking_id = response["bookingid"]
    assert response["booking"]["firstname"] == request.firstname
    assert response["booking"]["lastname"] == request.lastname
    assert str(response["booking"]["totalprice"]) == str(request.totalprice)
    assert str(response["booking"]["depositpaid"]) == str(request.depositpaid)
    assert response["booking"]["bookingdates"] == request.bookingdates
    assert response["booking"]["bookingdates"]["checkin"] == request.bookingdates["checkin"]
    assert response["booking"]["bookingdates"]["checkout"] == request.bookingdates["checkout"]
    assert response["booking"]["additionalneeds"] == request.additionalneeds

