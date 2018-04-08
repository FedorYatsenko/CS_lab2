# Decimal to 32-bit IEEE 754


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


dec = float(input("Input decimal: "))

res = 0

######################################
# знак
if dec < 0:
    res = 1 << 8
    dec *= -1

#######################################
# порядок

left = dec // 1
right = dec - left

first_one = 1  # iстиний порядок
i = 1

if left != 0:
    while i < left:
        i *= 2
        first_one += 1
    if i == left:
        first_one -= 1
    else:
        first_one -= 2
        i = i // 2
else:
    while i > right:
        i /= 2
        first_one -= 1
    first_one -= 1

print(first_one)
res += first_one + 127  # зсунутий порядок
res = res << 23

########################################
# мантиса

dec = dec - i
i = i / 2
shift = 22

print(dec, " ", i)
while shift >= 0 and dec != 0:
    if dec >= i:
        dec -= i
        res += 1 << shift

    shift -= 1
    i = i / 2

########################################

print("%s" % format(res, 'b'))
print_num(res)
