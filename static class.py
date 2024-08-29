class Person:
    city='chennai'
    area='adayar'
    def __init__(self, name, age, gender, occupation, location):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.location = location
    @classmethod
    def classname(cls):
        print("city aame",cls.city)
        print("area",cls.area)

    def print_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Occupation:", self.occupation)
        print("Location:", self.location)

person = Person("John Doe", 30, "Male", "Engineer", "New York")
person.print_details()
Person.classname()