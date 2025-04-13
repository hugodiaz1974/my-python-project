def categorize_ratings(rating_list):
    low = 0
    medium = 0
    high = 0
    for i in rating_list:
        if i >= 1 and i <=4:
            low += 1
        elif i >= 5 and i <= 7:
            medium += 1
        else:
            high += 1
    return low, medium, high 

low, medium, high = categorize_ratings([1, 3, 5, 7, 8, 9])

print("Low:", low)
print("Medium:", medium)
print("High:", high)
 