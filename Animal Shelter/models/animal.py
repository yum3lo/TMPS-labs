from abc import ABC, abstractmethod
from typing import List
from datetime import date
from patterns.observer.animal_observer import AnimalObserver
from patterns.builder.animal_profile import AnimalProfile

class Animal(ABC):
  def __init__(self, profile: AnimalProfile):
    self.profile = profile
    self._observers: List[AnimalObserver] = []

  def add_observer(self, observer: AnimalObserver):
    if observer not in self._observers:
      self._observers.append(observer)

  def remove_observer(self, observer: AnimalObserver):
    if observer in self._observers:
      self._observers.remove(observer)

  def notify_observers(self, message: str):
    for observer in self._observers:
      observer.update(self, message)

  @abstractmethod
  def make_sound(self):
    pass

  @abstractmethod
  def get_care_instructions(self):
    pass

  # observer-integrated updates
  def update_medical_history(self, condition: str):
    self.profile.medical_history.append(condition)
    self.notify_observers(f"Medical update: {condition}")

  def update_behavior_notes(self, note: str):
    self.profile.behavior_notes.append(note)
    self.notify_observers(f"Behavior update: {note}")

  def update_special_needs(self, need: str):
    self.profile.special_needs.append(need)
    self.notify_observers(f"Special needs update: {need}")

  def add_vaccination_status(self, vaccine: str, date: date):
    self.profile.vaccination_status[vaccine] = date
    self.notify_observers(f"Vaccination added: {vaccine} on {date}")


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