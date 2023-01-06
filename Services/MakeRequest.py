import requests
from Utilities.Configurations import *
from Payloads.Auth import *
from Payloads.CreateBooking import *
from Utilities.Resources import *

baseUrl = get_config()["API"]["endpoint"]
s = requests.Session()
s.headers = {'Content-Type': 'application/json'}


def make_request(method, resource, query_params, headers=None, path_variable=None):
    full_url = baseUrl + resource
    if path_variable is not None:
        full_url = full_url + "/" + path_variable

    response = s.request(method=method, url=full_url, json=query_params.__dict__, headers=headers, verify=False)
    return response


# class AuthResponse:
#     def __init__(self, token):
#         self.token = token

# class Test:
#
#     def test_auth(self):
#         response = make_auth_call(username="admin", password="password123")
#         assert response is not None
#         assert response.status_code == 200
#         data = response.json()
#         obj = AuthResponse(**data)
#         assert obj.token is not None
#
#     def xtest_create_booking(self):
#         br = BookingRequest(first_name="Shivam", last_name="Soni",
#                             total_price=20, deposit_paid=True,
#                             checkin="2011-02-02", checkout="2012-02-02",
#                             additional_needs="no more needs")
#
#         response = create_booking_request(br)
#         assert response is not None
#         assert response.status_code == 200
#         data = response.json()
#         obj = CreateBookingResponse(**data)
#         assert obj is not None