def calculate_purchase_price(purchase, set_to_dict=False):
    total = purchase['total']
    for i in purchase['books']:
        total = total + i['price']
    if set_to_dict == True:
        purchase['total'] = total
        return total
    else:
        return total
    

