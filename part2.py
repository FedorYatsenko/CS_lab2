# Зсув залишку вправо


def spc(string):
    print(string * 20)


def devide(dividend, divisor):

    quotient = 0

    shift = dividend.bit_length() - divisor.bit_length()

    while shift >= 0:
        quotient = quotient << 1

        print("  %20s" % format(dividend, 'b'), "  %20s" % format(quotient, 'b'))

        if dividend >= (divisor << shift):
            print("- %20s" % format((divisor << shift), 'b'))

            dividend -= divisor << shift
            quotient += 1

        spc("_")

        shift -= 1

    print("  %20s" % format(dividend, 'b'))

    return quotient


main_dividend = int(input("Input dividend: "), 2)
main_divisor = int(input("Input divisor: "), 2)

res = devide(main_dividend, main_divisor)

spc("#")
print("Quotient: ", "  %20s (" % format(res, 'b'),res, ")")
