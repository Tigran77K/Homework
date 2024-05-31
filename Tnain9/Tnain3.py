# Write a Python script that takes multiple text files as input and concatenates their contents into a single text file.
def contents_file(file1,file2 , file3):
    with open(file1,"r") as file:
        with open(file2, "r") as file_2:
            with open(file3 , "a") as file_3:
                for check1 in file:
                    for i in check1.split():
                        file_3.write(i + " ")
                for check2 in file_2:
                    for j in check2.split():
                        file_3.write(j + " ")
    return file3
input_file = "input.txt"
input_file1 = "input1.txt"
outinput_file = "output.txt"
print(contents_file(input_file,input_file1,outinput_file))