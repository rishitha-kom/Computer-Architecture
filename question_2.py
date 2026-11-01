# Rotate operations on 8-bit binary numbers

num = "10110110"

# (a) Rotate Left Without Carry (ROL)

print("Rotate Left Without Carry (ROL)")
print("Original number:", num)

for i in range(2):
    num = num[1:] + num[0]
    print("After rotation", i + 1, ":", num)

print("Final ROL result:", num)


# (b) Rotate Left With Carry (RCL)

num = "10110110"
carry = "0"

print("\nRotate Left With Carry (RCL)")
print("Original number:", num)
print("Initial Carry:", carry)

for i in range(2):
    new_carry = num[0]
    num = num[1:] + carry
    carry = new_carry
    print("After rotation", i + 1, ":", num)
    print("Carry:", carry)

print("Final RCL result:", num)
print("Final Carry:", carry)
