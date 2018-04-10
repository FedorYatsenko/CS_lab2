#        Алгоритм Бута


def spc(string):
    print(string * 20)


def inverse(value, sign):

    value = value ^ (2**(sign+1) - 1)
    value += 1
    value = value & (2**(sign+1) - 1)

    return value


def Booth(multiplicand, product, sign):
    for i in range(0, sign):
        print("multiplicand: %s" % format(multiplicand, 'b'))
        print("product: %s" % format(product, 'b'))

        if product & 3 == 1:
            print("01 add")
            print("  %11s" % format(product, 'b'))
            product += multiplicand << (sign + 1)
            product = product & (2**(2 * sign + 1) - 1)
            print("+ %11s" % format(multiplicand << (sign + 1), 'b'))
        elif product & 3 == 2:
            print("10 sub")
            print("  %11s" % format(product, 'b'))
            product += inverse(multiplicand, sign) << (sign + 1)
            product = product & (2**(2 * sign + 1) - 1)
            print("+ %11s" % format(inverse(multiplicand, sign) << (sign + 1), 'b'))
        else:
            print("00 or 11 nop")

        spc("_")
        print("  %11s" % format(product, 'b'))
        spc("#")

        if product & 2**(2 * sign):
            product += 2**(2 * sign + 1)

        product = product >> 1

    product = product >> 1
    return product


main_sign = int(input("Input sign position: "))

main_multiplicand = int(input("Input multiplicand: "), 2)
main_product = int(input("Input multiplier: "), 2)

print("  %10s" % format(main_multiplicand, 'b'))
print("* %10s" % format(main_product, 'b'))
print("Sign: ", main_sign)
spc("#")

main_product = main_product << 1

main_product = Booth(main_multiplicand, main_product, main_sign)

print("Result:")
print("  %11s" % format(main_product, 'b'))

if main_product & (2 ** (2 * main_sign - 1)):
    print("-", inverse(main_product, 2 * main_sign - 1))
else:
    print(main_product)
