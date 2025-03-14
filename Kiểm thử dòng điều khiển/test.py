from btkt import calculate_movie_ticket_price


def test_ticket_type_thuong():
    assert calculate_movie_ticket_price("thường", 19) == 150000
    assert calculate_movie_ticket_price("thường", 10) == 90000
    assert calculate_movie_ticket_price("thường", 15) == 100000


def test_ticket_type_vip():
    assert calculate_movie_ticket_price("VIP", 19) == 250000
    assert calculate_movie_ticket_price("VIP", 10) == 190000
    assert calculate_movie_ticket_price("VIP", 15) == 200000


def test_invalid_ticket_type():
    assert calculate_movie_ticket_price("invalid", 19) == -1


if __name__ == "__main__":
    test_ticket_type_thuong()
    test_ticket_type_vip()
    test_invalid_ticket_type()
