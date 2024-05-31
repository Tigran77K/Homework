#Print the multiplication table of 5 using a for loop and f”strings”. The table should be printed up to 10.
num = 0
num = int(num)
numb = num
stop = 10
for i in range(stop):
    num += 1
    numb = num
    print(f"{num} * 5 = {num *5}")
    if num == stop:
        break