from abc import ABC, abstractmethod
from models.animal import Animal, Dog, Cat
from ..builder.animal_profile import AnimalProfile

class AnimalFactory(ABC):
  @abstractmethod
  def create_animal(self, profile: AnimalProfile) -> Animal:
    pass

class GeneralFactory(AnimalFactory):
  def __init__(self, species: str):
    self.species = species
    
  def create_animal(self, profile: AnimalProfile) -> Animal:
    return self.species(profile)