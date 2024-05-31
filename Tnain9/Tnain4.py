# Develop a Python Function that reads a large text file (input.txt) and splits it
# into smaller files, each containing a specified number of lines. Function paramis
# ter the number of lines per file. Generate multiple output files (output1.txt, output2.txt, etc.).
def split_file(lennum, fileinput, file1, file2):
    stop = 0
    with open(fileinput, "r") as file_1:
        with open(file1, "a") as file_2:
            with open(file2, "a") as file_3:
                for line in file_1:
                    for word in line.split():
                        file_2.write(word + " ")
                        file_3.write(word + " ")
                        stop += 1
                        if stop == lennum:
                            return stop
                return stop
input_file = "input.txt"
input_file1 = "input1.txt"
outinput_file = "output.txt"
print(split_file(1, input_file , outinput_file , input_file1))