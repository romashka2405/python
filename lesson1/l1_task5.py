print("Введите две буквы")
a = input(">> ")
b = input(">> ")

offset = 96

pos_a = ord(a) - offset
pos_b = ord(b) - offset


print(f"№{a} в алфавите - {pos_a}")
print(f"№{b} в алфавите - {pos_b}")
print(f"Между ними {abs(pos_a - pos_b + 1)} букв")