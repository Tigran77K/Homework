#Write a Python script that reads a text file (input.txt) and counts the
# occurrences of each character (including spaces and punctuation). Output the
# character frequency to another text file (output.txt).
def special_test(file1,file2):
    spec = 0
    with open(file1,"r") as file:
        for i in file:
            for j in i:
                if not j.isalpha() or  j.isdigit():
                    spec += 1
        with open(file2,"a") as file_2:
            file_2.write(str(spec))
    return spec
input_file = "input.txt"
outinput_file = "output.txt"
print(special_test(input_file, outinput_file))