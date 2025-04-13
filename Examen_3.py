test_performance = {
    "John": 87,
    "Lisa": 90,
    "Mary": 75,
    "Chris": 100,
    "Linda": 100,
    "Matt": 70
}

# Create an empty list to store the scores
scores = []

# Use a for loop to extract each score
for score in test_performance.values():
    scores.append(score)

# Print the list of scores
print(scores)


def bubble_sort(scores):
    n = len(scores)
    # Traverse through all elements in the list
    for i in range(n):
        # Perform comparisons for the unsorted part of the list
        for j in range(0, n-i-1):
            # Swap if the element is greater than the next element
            if scores[j] > scores[j+1]:
                scores[j], scores[j+1] = scores[j+1], scores[j]
    return scores

# Example usage
scores = [87, 90, 75, 100, 100, 70]
sorted_scores = bubble_sort(scores)
print("Sorted scores:", sorted_scores)