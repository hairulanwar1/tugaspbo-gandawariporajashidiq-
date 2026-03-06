class Library:
    def __init__(self, library_name, book_type):
        self.library_name = library_name
        self.book_type = book_type

    def describe_library(self):
        print("Nama Perpustakaan:", self.library_name)
        print("Jenis Buku:", self.book_type)

    def open_library(self):
        print(self.library_name, "sekarang dibuka untuk pengunjung!")


# Membuat instance
library = Library("Perpustakaan Cerdas", "Buku Pendidikan")

# Menampilkan atribut
print(library.library_name)
print(library.book_type)

# Memanggil method
library.describe_library()
library.open_library()


class Library:
    def __init__(self, library_name, book_type):
        self.library_name = library_name
        self.book_type = book_type

    def describe_library(self):
        print("Nama Perpustakaan:", self.library_name)
        print("Jenis Buku:", self.book_type)
        print()


# Membuat 3 instance
lib1 = Library("Perpustakaan Digital", "Teknologi")
lib2 = Library("Perpustakaan Sejarah", "Sejarah")
lib3 = Library("Perpustakaan Anak", "Buku Anak")

# Memanggil method
lib1.describe_library()
lib2.describe_library()
lib3.describe_library()


class User:
    def __init__(self, first_name, last_name, age, email, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.city = city

    def describe_user(self):
        print("Nama:", self.first_name, self.last_name)
        print("Umur:", self.age)
        print("Email:", self.email)
        print("Kota:", self.city)

    def greet_user(self):
        print("Halo", self.first_name, "! Selamat datang.")
        print()


# Membuat instance
user1 = User("gan", "Ripo", 17, "Gandawa@email.com", "Pekanbaru")
user2 = User("Budi", "Santoso", 20, "budi@email.com", "Jakarta")
user3 = User("Siti", "Aisyah", 19, "siti@email.com", "Bandung")

# Memanggil method
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()