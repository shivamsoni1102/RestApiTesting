
def compare_create_booking(request, response):
    assert response["bookingid"] is not None
    assert response["booking"]["firstname"] == request.firstname
    assert response["booking"]["lastname"] == request.lastname
    assert str(response["booking"]["totalprice"]) == str(request.totalprice)
    assert str(response["booking"]["depositpaid"]) == str(request.depositpaid)
    assert response["booking"]["bookingdates"] == request.bookingdates
    assert response["booking"]["bookingdates"]["checkin"] == request.bookingdates["checkin"]
    assert response["booking"]["bookingdates"]["checkout"] == request.bookingdates["checkout"]
    assert response["booking"]["additionalneeds"] == request.additionalneeds


def compare_get_booking(request, response):
    assert response["firstname"] == request.firstname
    assert response["lastname"] == request.lastname
    assert str(response["totalprice"]) == str(request.totalprice)
    assert str(response["depositpaid"]) == str(request.depositpaid)
    assert response["bookingdates"] == request.bookingdates
    assert response["bookingdates"]["checkin"] == request.bookingdates["checkin"]
    assert response["bookingdates"]["checkout"] == request.bookingdates["checkout"]
    assert response["additionalneeds"] == request.additionalneeds