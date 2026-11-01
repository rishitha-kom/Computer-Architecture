# Signed binary arithmetic using 8-bit 2's complement

# Expression (a): 34 + (+27)

a = 34
b = 27

print("Expression (a): 34 + (+27)")

print("Binary of 34:", format(a & 255, '08b'))
print("Binary of 27:", format(b & 255, '08b'))

result = a + b

print("Result in binary:", format(result & 255, '08b'))
print("Result in decimal:", result)

if result > 127 or result < -128:
    print("Overflow: Yes")
else:
    print("Overflow: No")


# Expression (b): (-34) - (-27)

a = -34
b = -27

print("\nExpression (b): (-34) - (-27)")

print("Binary of -34:", format(a & 255, '08b'))
print("Binary of -27:", format(b & 255, '08b'))

result = a - b

print("Result in binary:", format(result & 255, '08b'))

if result >= 128:
    decimal_result = result - 256
else:
    decimal_result = result

print("Result in decimal:", decimal_result)

if result > 127 or result < -128:
    print("Overflow: Yes")
else:
    print("Overflow: No")
