from datetime import date
from patterns.adapter.notification_adapter import EmailNotification
from patterns.facade.shelter_facade import ShelterFacade

def main():
  shelter_facade = ShelterFacade(EmailNotification())

  shelter_facade.add_animal(
    name = "Mia", 
    species = "Cat", 
    age = 6,
    medical_history = ["Vaccinated", "Needs daily medication"],
    behavior_notes = ["Friendly"],
    special_needs = ["Grain-free diet"],
    medication = [
      {"name": "Painkillers", "schedule": "every 12 hours"},
      {"name": "Antibiotics", "schedule": "every 24 hours"}
    ],
    vaccination_status = {
      "Rabies": date(2021, 2, 1), 
      "FVRCP": date(2023, 6, 12)
    }
  )

  shelter_facade.add_animal(
    name = "Teddy", 
    species = "Dog", 
    age = 3,
    medical_history = ["Neutered", "Recent surgery"],
    behavior_notes = ["Energetic"],
    special_needs = ["Help exercise daily", "Add supplements to food"],
    medication = [
      {"name": "Painkillers", "schedule": "every 12 hours"}
    ],
    vaccination_status = {
      "Rabies": date(2023, 3, 21), 
      "Parvo": date(2021, 2, 1)
    }
  )

if __name__ == "__main__":
  main()