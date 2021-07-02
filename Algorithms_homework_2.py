def split_in_half(str):
    length = len(str)
    half = length //2
    add = 0
    if length % 2:
     add = 1
    left = str[:half + add]
    right = str[half + add:]
    return right + left

print(split_in_half("bbbbbcaaaaa"))

# Given a string, determine if it consists of all unique characters.
def uni_char(str):
    my_set = set(str)
    return len(str) == len(set(str))

print(uni_char('abcde'))
print(uni_char('aabcde'))


