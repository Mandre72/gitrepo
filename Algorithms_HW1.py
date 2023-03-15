# def sum_numbers(n: int):
#    final_sum = 0
#    for x in range(n + 1):
#        # final_sum = final_sum + x
#        final_sum += x

#    return final_sum


# test_n = 5
# result = sum_numbers(test_n)
# print(result)


# def find_max(a, b, c):
#    if a > b and a > c:
#        return a
#    if b > a and b > c:
#        return b
#    return c


# result = find_max(10, 20, 40)
# print(result)


def count_odd_even(n):
    odds = 0
    evens = 0

    while n != 0:
        current_digit = n % 10
        if current_digit % 2:
            odds += 1
        else:
            evens += 1
        n = n // 10

    print(f"Odd digit: {odds}")
    print(f"Even digits: {evens}")


test_n = 35680  # odds: 2, evens: 3
count_odd_even(test_n)

