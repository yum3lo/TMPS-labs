from abc import ABC, abstractmethod
from patterns.builder.animal_profile import AnimalProfile

class Animal(ABC):
  def __init__(self, profile: AnimalProfile):
    self.profile = profile

  @abstractmethod
  def make_sound(self):
    pass

  @abstractmethod
  def get_care_instructions(self):
    pass

class Dog(Animal):
  def make_sound(self):
    return "Woof"

  def get_care_instructions(self):
    return "Feed twice, Give fresh water, Go for a walk"

class Cat(Animal):
  def make_sound(self):
    return "Meow"

  def get_care_instructions(self):
    return "Feed three times, Give fresh water, Clean litter box"