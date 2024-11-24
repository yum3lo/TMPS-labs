from typing import List
from models.animal import Animal, Cat, Dog
from datetime import date
from patterns.builder.animal_profile import AnimalProfileBuilder
from patterns.singleton.shelter_management import ShelterManagement
from patterns.adapter.notification_adapter import NotificationManager
from patterns.decorator.animal_decorator import MedicalCareDecorator, SpecialNeedsDecorator
from patterns.observer.animal_observer import StaffObserver, VetObserver, OwnerObserver
from patterns.observer.observed_animal import ObservedCat, ObservedDog

class ShelterFacade:
  def __init__(self):
    self.shelter = ShelterManagement()
    self.notification_manager = NotificationManager()
    
    self.staff_observer = StaffObserver(self.notification_manager)
    self.vet_observer = VetObserver(self.notification_manager)
    self.owner_observer = OwnerObserver(self.notification_manager)

  def add_animal(self, name: str, species: str, age: int, medical_history: List[str], behavior_notes: List[str], special_needs: List[str], medication: List[dict], vaccination_status: dict) -> Animal:
    builder = AnimalProfileBuilder()
    builder.set_basic_info(name, species, age)
    profile = builder.build()
    
    if species.lower() == "cat":
      observed_animal = ObservedCat(profile)
    elif species.lower() == "dog":
      observed_animal = ObservedDog(profile)
    else:
      raise ValueError(f"Unsupported species: {species}")
          
    observed_animal.add_observer(self.staff_observer)
    observed_animal.add_observer(self.vet_observer)
    observed_animal.add_observer(self.owner_observer)
    
    for history in medical_history:
      observed_animal.update_medical_history(history)
    for note in behavior_notes:
      observed_animal.update_behavior_notes(note)
    for need in special_needs:
      observed_animal.update_special_needs(need)
    for vaccine, date in vaccination_status.items():
      observed_animal.add_vaccination_status(vaccine, date)
    for med in medication:
      observed_animal = MedicalCareDecorator(observed_animal, med["name"], med["schedule"])
    for need in special_needs:
      observed_animal = SpecialNeedsDecorator(observed_animal, need)
      
    self.shelter.add_animal(observed_animal)
    return observed_animal
  
  def list_animals(self):
    animals = self.shelter.list_animals()
    for animal in animals:
      print(f"Name: {animal.profile.name}, 
            Species: {animal.profile.species}, 
            Age: {animal.profile.age}",
            )