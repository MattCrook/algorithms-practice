import string




def tuple_slice(startIndex, endIndex, tup):
    t = tup[startIndex:endIndex]
    return ','.join(map(str,t))


print("tuple_slice", tuple_slice(1, 4, (76, 34, 13, 64, 12)))
print("-----------------------------")



def john_mary(str):
    formatted_string = str.lower()
    is_John = 'john' in formatted_string
    is_Mary = 'mary' in formatted_string
    condition = is_John and is_Mary
    if formatted_string.count('john') == formatted_string.count('mary'):
         return True
    else:
        return False

print("john_mary", john_mary('Mary&John'))
print("-----------------------------")



def numbers_to_letters_1(s):
    # it = iter(s)
    # map(''.join, zip(it, it))
    # map(int, map(''.join, zip(it, it)))
    # map(lambda n: chr(n + 96) if n < 27 else chr(n), map(int, map(''.join, zip(it, it))))
    # result = ''.join(map(lambda n : chr(n+96) if n < 27 else chr(n), map(int, map(''.join, zip(it,it)))))
    # return result
    it = iter(s)
    pairs = zip(it, it)
    map_its = map(''.join, pairs)
    map_pairs = map(int, map_its)
    l_to_n = map(lambda n: chr(n + 96) if n < 27 else chr(n), map_pairs)
    result = ''.join(l_to_n)
    return result

if __name__ == "__main__":
    print("numbers_to_letters_1", numbers_to_letters_1('20 5 19 20+4 15 13 5'))
print("-----------------------------")





def numbers_to_letters_2(s):
    it = iter(s)
    pairs = zip(it, it)
    if '+' in str(pairs):
        ind = pairs.index('+')
        print(ind)

    res = []
    for pair in zip(s[::2], s[1::2]):
        number = int("".join(pair))

        if number <= 26:
            number += 96

        res.append(chr(number))

    return "".join(res)
if __name__ == "__main__":
    print("numbers_to_letters_2", numbers_to_letters_2('20 5 19 20+4 15 13 5'))
print("-----------------------------")


def numbers_to_letters_3(s):
    for x, y in zip(range(1, 27), string.ascii_lowercase):
        print(x, y)

print("numbers_to_letters_3", numbers_to_letters_3('20 5 19 20+4 15 13 5'))
print("-----------------------------")
