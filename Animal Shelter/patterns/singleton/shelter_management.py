from typing import List
from models.animal import Animal

class ShelterManagement:
  _instance = None

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super().__new__(cls)
      cls._instance.animals = []
    return cls._instance

  def add_animal(self, animal: Animal):
    self.animals.append(animal)

  def list_animals(self) -> List[Animal]:
    return self.animals