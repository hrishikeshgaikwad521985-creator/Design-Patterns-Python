# factroy pattern
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def get_pet(pet_type):
    pets = dict(dog=Dog, cat=Cat)
    pet_class = pets.get(pet_type)
    return pet_class() if pet_class else None

dog = get_pet("dog")
cat = get_pet("cat")

print(dog.speak())
print(cat.speak())

# observer pattern
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received: {message}")

subject = Subject()
obs1 = Observer("Observer 1")
obs2 = Observer("Observer 2")

subject.attach(obs1)
subject.attach(obs2)
subject.notify("System Update Available")

# Singleton Pattern
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()

print(s1 is s2)

# stratergy pattern
class Add:
    def execute(self, a, b):
        return a + b

class Subtract:
    def execute(self, a, b):
        return a - b

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, a, b):
        return self.strategy.execute(a, b)

context_add = Context(Add())
print(context_add.execute_strategy(10, 5))

context_sub = Context(Subtract())
print(context_sub.execute_strategy(10, 5))