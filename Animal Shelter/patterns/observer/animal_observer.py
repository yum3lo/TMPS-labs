from abc import ABC, abstractmethod
from typing import List
from patterns.adapter.notification_adapter import NotificationManager

class AnimalObserver(ABC):
  def __init__(self, notification_manager: NotificationManager, role: str):
    self.notification_manager = notification_manager
    self.role = role

  @abstractmethod
  def update(self, animal: "Animal", message: str):
    pass

class StaffObserver(AnimalObserver):
  def __init__(self, notification_manager: NotificationManager):
    super().__init__(notification_manager, "staff")

  def update(self, animal: "Animal", message: str):
    full_message = (
      f"Name: {animal.profile.name}\n"
      f"Species: {animal.profile.species}\n"
      f"Update: {message}\n"
      f"Care Instructions: {animal.get_care_instructions()}"
    )
    self.notification_manager.notify(self.role, full_message)

class VetObserver(AnimalObserver):
  def __init__(self, notification_manager: NotificationManager):
    super().__init__(notification_manager, "vet")

  def update(self, animal: "Animal", message: str):
    full_message = (
      f"MEDICAL ALERT\n"
      f"Name: {animal.profile.name}\n"
      f"Species: {animal.profile.species}\n"
      f"Update: {message}\n"
      f"Medicine: {', '.join(animal.profile.medication)}\n"
      f"Medical History: {', '.join(animal.profile.medical_history)}"
    )
    self.notification_manager.notify(self.role, full_message)
    
class OwnerObserver(AnimalObserver):
  def __init__(self, notification_manager: NotificationManager):
    super().__init__(notification_manager, "owner")

  def update(self, animal: "Animal", message: str):
    full_message = (
      f"Name: {animal.profile.name}\n"
      f"Update: {message}\n"
    )
    self.notification_manager.notify(self.role, full_message)