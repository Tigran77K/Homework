# Implement a Python program that reads a text file (input.txt), prompts the user
# for a word to find, and another word to replace it with. Replace all occurrences of
# the first word with the second word and save the modified text to a new file (output.txt)
def replace_text (word, replace ,file1 , file2):
    stop = 0
    with open(file2, "a") as file_1:
        with open(file1,"r") as file:
            for i in file:
                for j in i.split():
                    if j != word:
                        file_1.write(str( j+ " "))
                    if j == word:
                        stop += 1
                        file_1.write(replace + " ")
            if stop == 0:
                return f"<{word}> not in the text"
    return word , replace
input_file = "input.txt"
outinput_file = "output.txt"
print(replace_text("hello" ,"hi" , input_file , outinput_file ))