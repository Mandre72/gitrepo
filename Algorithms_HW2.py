#def split_in_half(s):
#    length = len(s)
#    half = length // 2
#    add = 0
#    if length % 2:
#        add = 1
#    left = s[:half + add]
#    right = s[half + add:]
#    return right + left

# test_even = "aaabbb" # bbbaaa
# test_odd = "aaabbbb" #bbbaaab
# result_even = split_in_half(test_even)
# print(result_even)
# result_odd = split_in_half(test_odd)
# print(result_odd)


def uni_char(s):
    chars = set()

    for char in s:
        if char in chars:
            return False
        else:
            chars.add(char)

    return True


test_pos = "abcde"
test_neg = "abcdb"
result_pos = uni_char(test_pos)
print(result_pos)  # True
result_neg = uni_char(test_neg)
print(result_neg)  # False
