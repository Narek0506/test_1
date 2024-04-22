# ex 1
# def sector_area(r, alpha):
#     pi = math.pi
#     radius = math.radians(alpha)
#     S = (pi * r ** 2) * alpha / 360
#     return S
#
#
# print(sector_area(15, 120))

# ex 2
# def arabic_to_roman(num):
#     if not 0 < num < 4000:
#         return "invalid input"
#
#     roman_numerals = {
#         1000: "M",
#         900: "CM",
#         500: "D",
#         400: "CD",
#         100: "C",
#         90: "XC",
#         50: "L",
#         40: "XL",
#         10: "X",
#         9: "IX",
#         5: "V",
#         4: "IV",
#         1: "I"
#     }
#
#     result = ""
#     for key, value in sorted(roman_numerals.items(), reverse=True):
#         while num >= key:
#             result += value
#             num -= key
#     return result
#
#
# print(arabic_to_roman(16))


# ex 3
# def longest_word(n): big-O(n)
#     max_len_word = max(len(word) for word in n)
#     longest_words = [word for word in n if len(word) == max_len_word]
#     return longest_words
#
#
# list_1 = ["aba", "aa", "z", "ad", "vcd", "aba"]
# list_2 = ["aba", "aa", "z", "advc", "vcd", "aba"]
# print(longest_word(list_1))
# print(longest_word(list_2))
