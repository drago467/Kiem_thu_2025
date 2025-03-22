def calculate_movie_ticket_price(ticket_type, show_time):
    ticket_price = 0
    if ticket_type == "thường":
        ticket_price = 100000
    elif ticket_type == "VIP":
        ticket_price = 200000
    else:
        print("Loại vé không hợp lệ!")
        return -1

    if show_time >= 18:
        ticket_price += 50000
    elif show_time < 12:
        ticket_price -= 10000

    return ticket_price
