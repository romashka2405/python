a = 5
b = 6

print(bin(a + 2))
print(bin(a - 2))

print(
  a or b,
  a and b,
  a or not b,
  a and not b,
  a ^ b,
  sep="\n"
)