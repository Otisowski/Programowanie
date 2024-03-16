from classes import Library, Employee, Order, Book


def main():
    library1 = Library("Katowice City",
                       "Mariacka",
                       "40-014",
                       "8:00-22:00",
                       "123456789")

    library2 = Library("Gliwice",
                       "Szkolna",
                       "44-117",
                       "8:00-18:00",
                       "987654321")

    publication_date1 = "2024-01-09"
    book1 = Book(library1, publication_date1, "Sam", "Smith", 123)
    book2 = Book(library1, publication_date1, "Emma", "Klein", 221)
    book3 = Book(library2, publication_date1, "Rafael", "Kalkstein", 235)
    book4 = Book(library2, publication_date1, "Santiago", "Angry", 534)
    book5 = Book(library2, publication_date1, "Mitch", "Ham", 324)

    hire_date1 = "2018-04-23"
    hire_date2 = "2020-03-12"

    employee1 = Employee("Alice",
                         "Smith",
                         hire_date1,
                         "1993-12-21",
                         "Katowice",
                         "Bogucicka",
                         "40-014",
                         "321456987")
    employee2 = Employee("Bob",
                         "Johnson",
                         hire_date2,
                         "2000-04-01",
                         "Gliwice",
                         "Miejska",
                         "44-117",
                         "123654789")

    student1 = "Student1"
    student2 = "Student2"

    order1_books = [book1, book2, book3]
    order1_date = "2022-01-01"
    order1 = Order(employee1, student1, order1_books, order1_date)

    order2_books = [book4, book5]
    order2_date = "2022-01-02"
    order2 = Order(employee2, student2, order2_books, order2_date)

    print(order1)
    print()
    print(order2)


if __name__ == "__main__":
    main()