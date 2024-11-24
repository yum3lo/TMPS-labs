from typing import List
from models.animal import Animal, Dog, Cat
from patterns.builder.animal_profile import AnimalProfile
from patterns.observer.animal_observer import AnimalObserver

class ObservedAnimal(Animal):
  def __init__(self, profile: AnimalProfile):
    super().__init__(profile)
    self._observers: List[AnimalObserver] = []

  def add_observer(self, observer: AnimalObserver):
    if observer not in self._observers:
      self._observers.append(observer)

  def remove_observer(self, observer: AnimalObserver):
    self._observers.remove(observer)

  def notify_observers(self, message: str):
    for observer in self._observers:
      observer.update(self, message)

class ObservedDog(ObservedAnimal, Dog):
  pass

class ObservedCat(ObservedAnimal, Cat):
  pass