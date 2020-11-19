print("enter different three numbers of char")

a = int(input())
b = int(input())
c = int(input())

print("mid is")
if a > b > c or a < b < c:
  print(b)
elif b > c > a or b < c < a:
  print(c)
elif c > a > b or c < a < b:
  print(a)
