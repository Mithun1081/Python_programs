class Animal:
    def speak(self):
        print("Animal Speaking")
    #child class Dog inherits the base class Animal
class Dog(Animal):
    def bark(self):
        print("dog barking")
class DogChild(Dog):
    def eat(self):
        print("Eating bread...")
d = DogChild()
d.bark()
d.speak()
d.eat()