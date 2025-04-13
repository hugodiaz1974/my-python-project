def send_discount(books_purchased, discount_threshold, bonus_threshold):
    
    if books_purchased >= bonus_threshold:
        return print("Big discount applied!")
    elif books_purchased >= discount_threshold:
        return print("Discount applied!")
    else:
        return print("No discount.")
    
    
send_discount(3, 5, 10)
send_discount(7, 5, 10)
send_discount(12, 5, 10)