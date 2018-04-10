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


def devide_with_shift(dividend, divisor):
    res = 0

    remainder = dividend << 1
    print("Init remainder = %s" % format(remainder, 'b'))

    for i in range(0, dividend.bit_length()):
        res = res << 1
        remainder -= divisor << dividend.bit_length()

        spc("#")
        print("remainder = remainder – divisor = %s" % format(remainder, 'b'))

        if remainder < 0:
            remainder += divisor << dividend.bit_length()
            remainder = remainder << 1
            print("remainder < 0: remainder -> + divisor, shift 1; res -> shift")
        else:
            remainder = remainder << 1
            remainder += 1
            print("remainder >= 0: remainder -> shift 1, + 1; res -> +1, shift")
            res += 1

        print("remainder = %s" % format(remainder, 'b'))
        print("res = %s" % format(res, 'b'))

    return res


main_dividend = int(input("Input dividend: "), 2)
main_divisor = int(input("Input divisor: "), 2)
spc("#")

res = devide_with_shift(main_dividend, main_divisor)

spc("#")
print("%s (" % format(main_dividend, 'b'), main_dividend,
      ") /  %s (" % format(main_divisor, 'b'), main_divisor,
      ") =  %s (" % format(res, 'b'), res, ")")
