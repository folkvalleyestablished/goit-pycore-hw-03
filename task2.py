import random


def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000:
        return []

    if quantity > max - min + 1:
        return []

    numbers = random.sample(range(min, max + 1), quantity)
    numbers.sort()

    return numbers


print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(1, 5, 8))
