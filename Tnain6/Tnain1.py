#Write a Python function to find the Max of three numbers.
def max_num(num1, num2 , num3):
    if num1 > num2 > num3 or num1 > num3 > num2:
        print(f"max num > {num1}")
    elif num2 > num1 > num3 or num2 > num3 > num1:
        print(f"max num > {num2}")
    elif num3 > num2 >num1 or num3 >num1 >num2:
        print(f"max num > {num3}")
        return  num1,num2,num3
max_num(13,34,435)