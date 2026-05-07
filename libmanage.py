books = []

while True:
    print("\n1. Add Book")
    print("2. View Books")
    print("3. Remove Book")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        book = input("Enter book name: ")
        books.append(book)
        print("Book Added!")

    elif choice == '2':
        print("\nBooks Available:")
        for b in books:
            print("-", b)

    elif choice == '3':
        book = input("Enter book name to remove: ")
        books.remove(book)
        print("Book Removed!")

    elif choice == '4':
        break

    else:
        print("Invalid Choice")