class BookingRequest:
    def __init__(self, first_name, last_name, total_price: int,
                 deposit_paid: bool, checkin, checkout, additional_needs):
        self.firstname = first_name
        self.lastname = last_name
        self.totalprice: int = total_price
        self.depositpaid: bool = deposit_paid
        self.bookingdates = {
            "checkin": checkin,
            "checkout": checkout
        }
        self.additionalneeds = additional_needs
