from typing import List
from models.animal import Animal
from patterns.builder.animal_profile import AnimalProfileBuilder
from patterns.factory.animal_factory import CatFactory, DogFactory
from patterns.singleton.shelter_management import ShelterManagement
from patterns.adapter.notification_adapter import NotificationAdapter, NotificationSystem
from patterns.decorator.animal_decorator import MedicalCareDecorator, SpecialNeedsDecorator

class ShelterFacade:
  def __init__(self, notification_system: NotificationSystem):
    self.shelter = ShelterManagement()
    self.notification_adapter = NotificationAdapter(notification_system)

  def add_animal(self, name: str, species: str, age: int, medical_history: List[str], behavior_notes: List[str], special_needs: List[str], medication: List[dict], vaccination_status: dict) -> Animal:
    animal_profile_builder = AnimalProfileBuilder()
    animal_profile = animal_profile_builder.set_basic_info(name, species, age)

    for history in medical_history:
      animal_profile.add_medical_history(history)
    for note in behavior_notes:
      animal_profile.add_behavior_notes(note)
    for need in special_needs:
      animal_profile.add_special_needs(need)
    for vaccine, date in vaccination_status.items():
      animal_profile.add_vaccination_status(vaccine, date)
    
    profile = animal_profile.build()

    factory = CatFactory() if species.lower() == "cat" else DogFactory()
    animal = factory.create_animal(profile)

    for med in medication:
      med_name = med.get("name")
      med_schedule = med.get("schedule")
      animal = MedicalCareDecorator(animal, med_name, med_schedule)

    for need in special_needs:
      animal = SpecialNeedsDecorator(animal, need)

    # singleton for storing animal with decorators
    self.shelter.add_animal(animal)

    care_instructions = animal.get_care_instructions()
    vaccination_info = "Vaccinations:\n"
    for vaccine, vac_date in vaccination_status.items():
      vaccination_info += f"  - {vaccine}: {vac_date}\n"

    message = (
      f"Name: {name}\n"
      f"Species: {species}\n"
      f"Medical History: {', '.join(medical_history)}\n"
      f"{vaccination_info}"
      f"Behavior Notes: {', '.join(behavior_notes)}\n"
      f"Care Instructions: {care_instructions}\n"
    )

    # adapter for sending notifications
    self.notification_adapter.notify("staff@shelter.com", message)

    return animal