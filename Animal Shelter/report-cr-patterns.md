# Laboratory Work 1: Creational Design Patterns

## Task
Define the main involved classes and think about what instantiation mechanisms are needed. Implement at least 3 creational design patterns in your project.

I implemented the Singleton, Builder and Factory patterns in a python project that manages a shelter catalog.

## Implementation

### Singleton Pattern (`ShelterManagement`)
Ensures only one instance of the shelter management system exists, maintains a central registry of all animals (cats and dogs) and is a single point of control for the entire system. I defined a private class variable `_instance` that stores the single instance of the class. The `__new__` method checks if an instance exists and if it doesn't, it creates one. The new instance is stored in `_instance` and initialized with an empty animals list.

```python
_instance = None

def __new__(cls):
    if cls._instance is None:
        cls._instance = super().__new__(cls)
        cls._instance.animals = []
    return cls._instance
```

The `add_animal` function adds a new animal to the shelter's registry and the `list_animals` gets the complete list of animals in the shelter.

```python
def add_animal(self, animal: Animal):
    self.animals.append(animal)

def list_animals(self) -> List[Animal]:
    return self.animals
```

### Builder Pattern (`AnimalProfileBuilder`)
Handles the construction of complex `AnimalProfile` objects, makes it easy to create different species of animals with different attributes and provides a simple interface.

The `AnimalProfile` class initializes all attributes with default values and their data structures.

```python
self.name = None
self.species = None
self.age = None
self.medical_history = []
self.behavior_notes = []
self.special_needs = []
self.vaccination_status = {}
```

The constructor creates a new `AnimalProfile` instance.

```python
def __init__(self):
    self.profile = AnimalProfile()
```

The `set_basic_info` method sets obligatory basic information, uses type hints to validate the parameters.

```python
def set_basic_info(self, name: str, species: str, age: int):
    self.profile.name = name
    self.profile.species = species
    self.profile.age = age
    return self
```

Each of the following methods adds a single item to its own collection and allows for more additions through method chaining.

```python
def add_medical_history(self, condition: str):
    self.profile.medical_history.append(condition)
    return self

def add_behavior_notes(self, note: str):
    self.profile.behavior_notes.append(note)
    return self

def add_special_needs(self, need: str):
    self.profile.special_needs.append(need)
    return self
```

The `add_vaccination_status` method uses a dictionary to store the vaccine history and links each vaccine with its administration date.

```python
def add_vaccination_status(self, vaccine: str, date_administered: date):
    self.profile.vaccination_status[vaccine] = date_administered
    return self
```

The `build` method returns the fully constructed `AnimalProfile` object and is the final step in the building process.

```python
def build(self):
    return self.profile
```

### Factory Method Pattern (`AnimalFactory`)
Gives an interface for creating animals, lets the subclasses (`CatFactory`, `DogFactory`) decide which class to instantiate. It also makes the system extensible for new animal types and encapsulates the logic for object creation. The abstract AnimalFactory class uses `@abstractmethod` to make it obligatory to be implemented and provides a simple interface for all animal factories.

```python
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self, profile: AnimalProfile) -> Animal:
        pass
```

The child classes inherit from `AnimalFactory` and implement `create_animal` methods to return Dog and Cat instances. They use the profile provided by `AnimalProfile` for initialization.

```python
class DogFactory(AnimalFactory):
    def create_animal(self, profile: AnimalProfile) -> Animal:
        return Dog(profile)

class CatFactory(AnimalFactory):
    def create_animal(self, profile: AnimalProfile) -> Animal:
        return Cat(profile)
```

The `animal.py` file defines the key animal classes using abstract base classes and inheritance.

```python
def __init__(self, profile: AnimalProfile):
    self.profile = profile

@abstractmethod
def make_sound(self):
    pass

@abstractmethod
def get_care_instructions(self):
    pass
```

The `Dog` and `Cat` classes implement required abstract methods, providing dog/cat specific behaviors by maintaining the contract defined by `Animal` class.

```python
class Dog(Animal):
    def make_sound(self):
        return "Woof"
    
    def get_care_instructions(self):
        return "Feed twice a day, walk daily, fresh water"

class Cat(Animal):
    def make_sound(self):
        return "Meow"
    
    def get_care_instructions(self):
        return "Feed three times a day, fresh water, clean litter box"
```

I created empty `__init__.py` files in each directory to make them Python packages. The `main.py` file serves as the entry point and demonstration of how the implemented design patterns work together in the `Animal Shelter` system.

For the Singleton Pattern it ensures only one shelter management system exists throughout the application and all operations on animals go through this single instance.

```python
shelter = ShelterManagement()
```

For the Builder Pattern it creates detailed profiles with basic information (name, species, age), medical history, behavior notes and vaccination records.

```python
cat_profile_builder = AnimalProfileBuilder()
cat_profile = (
    cat_profile_builder
    .set_basic_info("Mia", "Cat", 6)
    .add_medical_history("Vaccinated")
    .add_behavior_notes("Friendly")
    .add_vaccination_status("Rabies", date(2021, 2, 1))
    .build()
)
```

And for the Factory Pattern it uses specific factories for each animal type and shows how factories handle the object creation process.

```python
cat_factory = CatFactory()
new_cat = cat_factory.create_animal(cat_profile)
shelter.add_animal(new_cat)
```

## Conclusions

This project uses 3 design patterns: Singleton, Builder and Factory. The main benefits of using these patterns in this project are centralized management (Singleton ensures consistent access to the shelter system), flexible construction (Builder allows creating detailed animal profiles without constructor complexity) and extensible creation (Factory Method makes it easy to add new animal types). This project shows how all three patterns work together: the Builder creates the profile, the Factory creates the animal with the profile and the Singleton manages all created animals.
