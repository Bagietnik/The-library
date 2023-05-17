from datetime import datetime, timedelta

class Material:
    def __init__(self, title, author, publication_date):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.borrowed_by = None

    def __str__(self):
        return f"{self.title} ({self.publication_date}) by {self.author}"


class PrintedMaterial(Material):
    def __init__(self, title, author, publication_date, isbn):
        super().__init__(title, author, publication_date)
        self.isbn = isbn

    def __str__(self):
        return super().__str__() + f" ISBN: {self.isbn}"


class Film(Material):
    def __init__(self, title, author, publication_date, duration):
        super().__init__(title, author, publication_date)
        self.duration = duration

    def __str__(self):
        return super().__str__() + f" Duration: {self.duration} minutes"


class Library:
    def __init__(self):
        self.materials = []

    def list_materials(self):
        for material in self.materials:
            print(material)

    def add_material(self, material):
        self.materials.append(material)

    def remove_material(self, material):
        if material in self.materials:
            self.materials.remove(material)
            print(f"Removed {material} from the library.")
        else:
            print("Material not found in the library.")


class Borrower:
    def __init__(self, name):
        self.name = name
        self.borrowed_materials = []

    def borrow_material(self, material, days):
        if material.borrowed_by is not None:
            print("Material is already borrowed.")
        else:
            material.borrowed_by = self
            due_date = datetime.now() + timedelta(days=days)
            self.borrowed_materials.append((material, due_date))
            print(f"{self.name} has borrowed {material} until {due_date}.")

    def return_material(self, material):
        if material.borrowed_by == self:
            material.borrowed_by = None
            self.borrowed_materials = [item for item in self.borrowed_materials if item[0] != material]
            print(f"{self.name} has returned {material}.")
        else:
            print("Material was not borrowed by this person.")

    def list_borrowed_materials(self):
        if self.borrowed_materials:
            print(f"{self.name} has borrowed the following materials:")
            for item in self.borrowed_materials:
                material, due_date = item
                print(f"- {material} (due date: {due_date})")
        else:
            print(f"{self.name} has no borrowed materials.")


class Student(Borrower):
    def __init__(self, name):
        super().__init__(name)
        self.max_borrowing_days = 30


class Staff(Borrower):
    def __init__(self, name):
        super().__init__(name)
        self.max_borrowing_days = 45


#the library init
library = Library() #inicjalizacja biblioteki

#the book object init
book = PrintedMaterial("Book Title", "Author Name", "2022", "1234567890")

#adding the book to library
library.add_material(book)

#the book object init
movie = Film("Movie Title", "Director Name", "2023", 120)

#adding the movie to library
library.add_material(movie)

#print of library collection
library.list_materials()

#user "student" init
student = Student("John")

#student is borrowing the material
student.borrow_material(book, 25)

#user "staff" init
staff = Staff("Jane")

#staff is borrowing the material
staff.borrow_material(book, 40)

while True:
    print("\nLibrary Management System")
    print("1. List materials")
    print("2. Add material")
    print("3. Remove material")
    print("4. Borrow material")
    print("5. Return material")
    print("6. List borrowed materials")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nMaterials in the library:")
        library.list_materials()
    elif choice == "2":
        print("\nAdd Material")
        title = input("Enter the title: ")
        author = input("Enter the author/director: ")
        publication_date = input("Enter the publication date: ")
        material_type = input("Enter the material type (1 for printed material, 2 for film): ")
        if material_type == "1":
            isbn = input("Enter the ISBN: ")
            material = PrintedMaterial(title, author, publication_date, isbn)
        elif material_type == "2":
            duration = input("Enter the duration in minutes: ")
            material = Film(title, author, publication_date, duration)
        else:
            print("Invalid material type.")
            continue
        library.add_material(material)
        print("Material added to the library.")
    elif choice == "3":
        print("\nRemove Material")
        title = input("Enter the title of the material to remove: ")
        for material in library.materials:
            if material.title == title:
                library.remove_material(material)
                break
        else:
            print("Material not found in the library.")
    elif choice == "4":
        print("\nBorrow Material")
        borrower_type = input("Enter the borrower type (1 for student, 2 for staff): ")
        name = input("Enter the borrower name: ")
        days = int(input("Enter the borrowing duration in days: "))
        if borrower_type == "1":
            borrower = Student(name)
        elif borrower_type == "2":
            borrower = Staff(name)
        else:
            print("Invalid borrower type.")
            continue
        print("\nMaterials in the library:")
        library.list_materials()
        title = input("Enter the title of the material to borrow: ")
        for material in library.materials:
            if material.title == title:
                borrower.borrow_material(material, days)
                break
        else:
            print("Material not found in the library.")
    elif choice == "5":
        print("\nReturn Material")
        borrower_type = input("Enter the borrower type (1 for student, 2 for staff): ")
        name = input("Enter the borrower name: ")
        if borrower_type == "1":
            borrower = Student(name)
        elif borrower_type == "2":
            borrower = Staff(name)
        else:
            print("Invalid borrower type.")
            continue
        print(f"\nMaterials borrowed by {borrower.name}:")
        borrower.list_borrowed_materials()
        title = input("Enter the title of the material to return: ")
        for material, _ in borrower.borrowed_materials:
            if material.title == title:
                borrower.return_material(material)
                break
        else:
            print("Material not found or not borrowed by this person.")
    elif choice == "6":
        print("\nList Borrowed Materials")
        borrower_type = input("Enter the borrower type (1 for student, 2 for staff): ")
        name = input("Enter the borrower name: ")
        if borrower_type == "1":
            borrower = Student(name)
        elif borrower_type == "2":
            borrower = Staff(name)
        else:
            print("Invalid borrower type.")
            continue
        borrower.list_borrowed_materials()
    elif choice == "0":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the Library Management System!")