def calculate_order(price, cash_coupon, percent_coupon):
    tax = 0.06
    subtotal = (price - cash_coupon)*(1-percent_coupon)

    if subtotal < 0:
        subtotal  = 0
    if 0 <= price < 10:
        shipping = 5.95
    elif 10 <= price < 30:
        shipping = 7.95
    elif 30 <= price < 50:
        shipping = 11.95
    elif 50 <= price:
        shipping = 0


    return subtotal*(1+tax)+shipping


if __name__ == '__main__':

    calculate_price()
