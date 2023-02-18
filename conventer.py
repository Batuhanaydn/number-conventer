class Binary:
    def binary_converter(number):
        return format(number, 'b')

class Octal:
    def octal_converter(number):
        return format(number, 'o')

class Hexedecimal:
    def hexedecimal_converter(number):
        return format(number, '02x')

class CustomBase:
    def custom_base_converter(number, base):
        result = ""
        if number == 0:
            return [0]
        digits = []
        while number:
            digits.append(int(number % base))
            number //= base
        for i in digits[::-1]:
            result += str(i)
        return str(base)+"b"+result

# print(Octal.octal_converter())
print(Hexedecimal.hexedecimal_converter(16))
print(CustomBase.custom_base_converter(6,3))