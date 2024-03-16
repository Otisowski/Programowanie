from classes import Student


def main():
    student1 = Student("Dan", [60, 70, 80])

    print(f"Student '{student1.name}' "
          f"{'' if student1.is_passed() else 'did not'} pass the exam.")

if __name__ == "__main__":
    main()