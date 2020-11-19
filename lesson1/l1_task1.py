print("введи целое трехзначное число")
n = int(input())
if len(str(n)) == 3:
    a = int(n / 100)
    b = int((n - (a * 100)) / 10)
    c = n - a*100 - b*10
    print(f"the product of the numbers = {a * b * c}")
    print(f"the sum of the numbers = {a + b + c}")
else:
  print("not three digits in n")
