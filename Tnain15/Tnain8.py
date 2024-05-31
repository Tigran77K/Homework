#Create a dictionary of book titles and their authors. Write a function to search for a book by its title and return the author's name.
books = {"War and Peace":"Leo Tolstoy" , "Harry Potter" :"Joanne Rowling" , "Moby-Dick" : "Herman Melville"}
def search_book(books, title):
    if title in books:
        return books[title]
    else:
        return "Book not found"
print(search_book(books,"Harry Potter"))