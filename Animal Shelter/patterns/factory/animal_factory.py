from abc import ABC, abstractmethod
from models.animal import Animal, Dog, Cat
from ..builder.animal_profile import AnimalProfile

class AnimalFactory(ABC):
  @abstractmethod
  def create_animal(self, profile: AnimalProfile) -> Animal:
    pass

class DogFactory(AnimalFactory):
  def create_animal(self, profile: AnimalProfile) -> Animal:
    return Dog(profile)

class CatFactory(AnimalFactory):
  def create_animal(self, profile: AnimalProfile) -> Animal:
    return Cat(profile)