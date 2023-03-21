def takeoff(num_books):
    global books_left
    global books_taken
    books_taken = books_left[:num_books]
    books_left = books_left[num_books:]
    return books_taken

def puton(new_books):
    global books_left
    global books_taken
    books_left += new_books
    books_taken = []

books_left = ["Python"] * 10
books_taken = []

while True:
    print("Books in the layer:", len(books_left))
    num_books = int(input("How many books do you want to take off? "))
    taken = takeoff(num_books)
    print("Books taken:", len(taken))
    print("Books left:", len(books_left))
    if len(books_left) == 0:
        print("No more books left!")
        break
    new_books = input("Enter the titles of the books you are putting back on (separated by commas): ").split(",")
    puton(new_books)


