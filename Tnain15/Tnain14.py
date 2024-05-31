#Write a function that capitalizes the first letter of each word in a sentence
def capitalize_first_letter(sentence):
    new_sentence = ""
    for word in sentence.split():
        new_sentence += word[0].upper() + word[1:] + " "
    return new_sentence
print(capitalize_first_letter("hello world"))
