# IEEE 754 Floating Point Множення

"""
1. Compute exponents
2. Multiply significands
3. Normalize result
4. Set sign
"""


def mult(num1, num2):
    if (num1 >> 23) & 255 == 0 or (num2 >> 23) & 255 == 0:
        return 0

    ######################################################
    res = ((num1 >> 31) ^ (num2 >> 31)) << 31

    print("Sign: ", (num1 >> 31), " xor ", (num2 >> 31), " = ", ((num1 >> 31) ^ (num2 >> 31)))
    ######################################################

    m1 = num1 & 8388607
    m2 = num2 & 8388607

    mantissa = (1.0 + m1 / 8388608) * (1.0 + m2 / 8388608)

    print("mantissa = 1.%s" % format(m1, 'b'), "* 1.%s" % format(m2, 'b'))
    ######################################################

    shift = 0

    while mantissa >= 2:
        shift += 1
        mantissa /= 2

    mantissa = ((mantissa - 1) * 8388608) // 1

    res += int(mantissa)

    print("Normalize mantissa: 1.%s" % format(int(mantissa), 'b'), ", shift: ", shift)
    ######################################################

    e1 = (num1 >> 23) & 255
    e2 = (num2 >> 23) & 255

    exponent = (e1 - 127) + (e2 - 127) + shift + 127

    res += exponent << 23

    print("Exponent: (%s - 1111111)" % format(e1, 'b'), " + (%s - 1111111)" % format(e2, 'b'),
          " + %s" % format(shift, 'b'), " + 1111111")
    ######################################################

    return res


def print_num(num):
    res = ""

    for i in range(0, 5):
        res = "_%4s" % format(num & 15, 'b') + res
        num = num >> 4

    res = "|%3s" % format(num & 7, 'b') + res
    num = num >> 3

    res = "_%4s" % format(num & 15, 'b') + res
    num = num >> 4

    res = "|%4s" % format(num & 15, 'b') + res
    num = num >> 4

    res = "%s" % format(num, 'b') + res

    print(res)


main_num1 = int(input("Input num1: "), 2)
main_num2 = int(input("Input num2: "), 2)

print_num(main_num1)
print_num(main_num2)
print("_________________________________________")

main_res = mult(main_num1, main_num2)
print("_________________________________________")
print_num(main_res)
