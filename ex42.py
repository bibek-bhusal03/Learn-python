## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass
## Dog is a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has a name
        self.name = name

## Cat is a Animal
class Cat(Animal):
    def __init__(self, name):
        ## Cat has a name
        self.name = name
## Person is-a object
class Person(object):
    def __init__(self, name):
        ## Person has-a name
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Persona
class Employee(Person):
    def __init__(self, name, salary):
        ## Employee is a Person, so initialize persona with name
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is a Object
class Fish(object):
    pass

## Salmon ia a Fish
class Salmon(Fish):
    pass

## Halibut is a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")
## satan is-a Cat
satan = Cat("Satan")
## mary ia a Person
mary = Person("Mary")
## marry's pet is satan
mary.pet = satan
## Frank is-a Employee 
frank = Employee("Frank", 120000)
## franks pet is rover 
frank.pet = rover
## flipper is a Fish
flipper = Fish()
## crouse is a Salmon
crouse = Salmon()
## harry is a Halibut
harry = Halibut()