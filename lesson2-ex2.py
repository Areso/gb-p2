import json


def write_order_to_json(item, quantity, price, buyer, bdate):
    myorder = {}
    myorder["item"] = item
    myorder["quantity"] = quantity
    myorder["price"] = price
    myorder["buyer"] = buyer
    myorder["bdate"] = bdate
    print(myorder)
    with open('order.json', 'w') as f_n:
        json.dump(myorder, f_n, skipkeys=True, indent=4)
    return 0


write_order_to_json('book', '1', '1500 RUB', 'Anton', '2018-12-22')


