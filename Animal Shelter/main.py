from datetime import date
from patterns.facade.shelter_facade import ShelterFacade

def main():
  shelter_facade = ShelterFacade()
  shelter_facade.notification_manager.set_contact_preference(
    role="staff", contact_type="email", contact="staff@example.com"
  )
  shelter_facade.notification_manager.set_contact_preference(
    role="vet", contact_type="sms", contact="+1234567890"
  )
  shelter_facade.notification_manager.set_contact_preference(
    role="owner", contact_type="email", contact="owner@example.com"
  )

  animals = [
    {
      "name": "Mia",
      "species": "Cat",
      "age": 6,
      "medical_history": ["Vaccinated", "Needs daily medication"],
      "behavior_notes": ["Friendly"],
      "special_needs": ["Grain-free diet"],
      "medication": [
        {"name": "Painkillers", "schedule": "every 12 hours"},
        {"name": "Antibiotics", "schedule": "every 24 hours"}
      ],
      "vaccination_status": {
        "Rabies": date(2021, 2, 1),
        "FVRCP": date(2023, 6, 12)
      }
    },
    {
      "name": "Teddy",
      "species": "Dog",
      "age": 3,
      "medical_history": ["Neutered", "Recent surgery"],
      "behavior_notes": ["Energetic"],
      "special_needs": ["Help exercise daily", "Add supplements to food"],
      "medication": [
        {"name": "Painkillers", "schedule": "every 12 hours"}
      ],
      "vaccination_status": {
        "Rabies": date(2023, 3, 21),
        "Parvo": date(2021, 2, 1)
      }
    }
  ]
  
  for animal_data in animals:
    shelter_facade.add_animal(**animal_data)
  
  animals_list = shelter_facade.shelter.list_animals()
  if animals_list:
    animals_list[0].update_medical_history("New allergy detected")

if __name__ == "__main__":
  main()