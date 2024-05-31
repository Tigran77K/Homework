# Write a function that prompts the user to enter a number and tries to convert it to an
# integer. Handle the TypeError exception by printing a message indicating that the input
# is not a valid number. Use a finally block to print "Type conversion process completed."
def convert_num(num):
    try:
        num = int(num)
    except:
        print("Uncorrected number entered")
    finally:
        print("Type conversion process completed.")
    return num
print(convert_num(3))