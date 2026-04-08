books_list = []
authors_set = set()
books_dict = {}
books_list.append ("Python Programming")
authors_set.add("John Smith")
books_dict["Python Programming"] = "John Smith"

books_list.append ("Python Fundamentals")
authors_set.add("John Smith")
books_dict["Python Fundamentals"] = "John Smith"

books_list.append ("Data Structures and Algorithms")
authors_set.add("Jane Doe")
books_dict["Data Structures and Algorithms"] = "Jane Doe"

books_list.append ("Machine Learning Basics")
authors_set.add("Alice Johnson")
books_dict["Machine Learning Basics"] = "Alice Johnson"
#search for a books
search_title = input("Enter the title od the books to search:")
if search_title in books_list:
    print(f"Books found! The Author of the books {search_title} is {books_dict [search_title]}")
else:
    print("Book not found!")
#remove a book from the list, set, and dictionary
remove_title = input ("Enter the title of the book to remove or else enter to skip :")
if remove_title in books_list:
    remove_author = books_dict[remove_title]
    books_list.remove(remove_title)
    del books_dict[remove_title]

    if remove_author not in books_dict.values():#check if the author has any other books in the dictionary
       authors_set.remove(remove_author)


    print("Book removed successfully!")
    print("Books available along with their authors:", books_dict)
    print("Just available books:", books_list)
    print("Just avilable authors:", authors_set)
else:
    print("Book not found!")