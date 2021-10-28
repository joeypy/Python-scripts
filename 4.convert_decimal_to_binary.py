def convert_to_binary(decimal):
    binary = []

    remainder = decimal % 2
    quotient = decimal // 2
    binary.insert(0, remainder)

    while True:
        remainder = quotient % 2
        quotient = quotient // 2
        binary.insert(0, remainder)
        if quotient == 0:
            break
    str_binary = ''
    for num in binary:
        str_binary = str_binary + str(num)

    print(f"\nNumber in decimal: {decimal}")
    print(f"Number in binary: 0b{str_binary}\n")


def convert_to_hex(decimal):
    hexadecimal = []
    remainder = decimal % 16
    quotient = decimal // 16
    hexadecimal.append(remainder)

    while True:
        remainder = quotient % 16
        quotient = quotient // 16
        hexadecimal.append(remainder)
        if quotient == 0:
            break
    str_hex = ''

    for num in hexadecimal:
        if num >= 0 and num <= 9:
            str_hex = str(num) + str_hex
        elif num == 10:
            str_hex = 'A' + str_hex
        elif num == 11:
            str_hex = 'B' + str_hex
        elif num == 12:
            str_hex = 'C' + str_hex
        elif num == 13:
            str_hex = 'D' + str_hex
        elif num == 14:
            str_hex = 'E' + str_hex
        elif num == 15:
            str_hex = 'F' + str_hex
    print(f"\nNumber in decimal: {decimal}")
    print(f"Number in hexadecimal: 0x{str_hex}\n")


def convert_to_octal(decimal):
    octal = []
    remainder = decimal % 8
    quotient = decimal // 8
    octal.insert(0, remainder)

    while True:
        remainder = quotient % 8
        quotient = quotient // 8
        octal.insert(0, remainder)
        if quotient == 0:
            break
    str_octal = ''
    for num in octal:
        str_octal = str_octal + str(num)
    print(f"\nNumber in decimal: {decimal}")
    print(f"Number in Octal: {str_octal}\n")


convert_to_binary(111)
convert_to_hex(1991)
convert_to_octal(1852)
