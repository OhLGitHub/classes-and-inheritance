class Animal:
    """
    This is a class for animals.
      
    Attributes:
        name (str): The name of the animal.
        age (int): The age of the animal in years.
        habitat (str): The natural habitat of the animal.
    
    Methods:
        breathe(): Checks if the animal is breathing.
    """
    def __init__(self, name, age, habitat):
        print('Initializing name, age, habitat')
        self.__name = name
        self.__age = age
        self.__habitat = habitat

    def breathe(self):
        print("Breathing")

class Fish(Animal):
    """
    This is a class for fish, inheriting from Animal.
    
    Methods:
        move(): Moves the animal.
    """
    def move(self):
        print("Swimming")

class Snake(Animal):
    """
    This is a class for snakes, inheriting from Animal.
    
    Methods:
        move(): Moves the animal.
        vocalize(): Causes the animal to vocalize.
    """
    def move(self):
        print("Slithering")

    def vocalize(self):
        print("Hissing")

class Person(Animal):
    """
    This is a class for people, inheriting from Animal.
    
    Methods:
        move(): Moves the animal.
        vocalize(): Causes the animal to vocalize.
    """
    def move(self):
        print("Error: Person is tied to laptop 24/7 and cannot move")

    def vocalize(self):
        print("Yelling,'SAVE ME FROM BOOTCAMP'")

class Book:
    """
    This is a class for books.
      
    Attributes:
        name (str): The name of the book.
        author (str): The author(s) of the book.
        isbn (int): The ISBN of the book.
    
    Methods:
        read(): Causes the book to be read.
    """
    def __init__(self, name, author, isbn):
        print('Initializing name, author, isbn')
        self.__name = name
        self.__author = author
        self.__isbn = isbn
    
    def read(self):
        print("Reading")

class Textbook(Book):
    """
    This is a class for textbooks, inheriting from Book.
      
    Methods:
        set_on_fire(): Causes the textbook to be set on fire.
    """
    def set_on_fire(self):
        print("Burning (after the semester is over)")

class Addressbook(Book):
    """
    This is a class for addressbooks, inheriting from Book.

    Methods:
        recycle(): Places the addressbook in the recycling bin.
    """
    def recycle(self):
        print("Recycling")

class Vehicle:
    """
    This is a class for vehicles.
      
    Attributes:
        color (str): The vehicle color.
        mode_of_tr (str): The vehicle's mode of transportation.
    
    Methods:
        move(): Moves the vehicle.
        stop(): Stops the vehicle.
    """
    def __init__(self, color, mode_of_tr):
        self.__color = color
        self.__mode_of_tr = mode_of_tr
    
    def move(self):
        print("Moving")
    
    def stop(self):
        print("Stopped moving")

class Car(Vehicle):
    """
    This is a class for cars, inheriting from Vehicle.
      
    Attributes:
        make (str): The vehicle make.
        model (str): The vehicle model.
    """
    def __init__(self, make, model):
        self.__make = make
        self.__model = model

class Bicycle(Vehicle):
    """
    This is a class for bicycles, inheriting from Vehicle.
      
    Methods:
        annoy(): Annoys drivers.
    """
    def annoy(self):
        print("Annoying drivers by taking up the entire lane")

class Boat(Vehicle):
    """
    This is a class for boats, inheriting from Vehicle.
      
    Methods:
        sink(): Sinks the boat.
    """
    def sink(self):
        print("Causing Dev10 applicants to decide on 15 essential survival items")

class Hot_Air_Balloon(Vehicle):
    """
    This is a class for boats, inheriting from Vehicle.
      
    Methods:
        inflate(): Inflates the balloon.
        deflate(): Deflates the balloon.
    """
    def inflate(self):
        print("Inflating")

    def deflate(self):
        print("Deflating")