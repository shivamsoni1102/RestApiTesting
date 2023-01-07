
create_token = "/auth"


def get_booking(book_id: str):
    return '/booking/{}'.format(book_id)


create_booking: str = "/booking"


def update_booking(book_id: str):
    return '/booking/{}'.format(book_id)


def delete_booking(book_id: str):
    return '/booking/{}'.format(book_id)
