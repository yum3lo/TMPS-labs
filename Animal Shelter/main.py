from datetime import date
from patterns.singleton.shelter_management import ShelterManagement
from patterns.builder.animal_profile import AnimalProfileBuilder
from patterns.factory.animal_factory import CatFactory, DogFactory

def main():
  # cat
  shelter = ShelterManagement()

  cat_profile_builder = AnimalProfileBuilder()
  cat_profile = (
    cat_profile_builder
    .set_basic_info("Mia", "Cat", 6)
    .add_medical_history("Vaccinated")
    .add_behavior_notes("Friendly")
    .add_vaccination_status("Rabies", date(2021, 2, 1))
    .build()
  )

  cat_factory = CatFactory()
  new_cat = cat_factory.create_animal(cat_profile)

  shelter.add_animal(new_cat)

  # dog
  dog_profile_builder = AnimalProfileBuilder()
  dog_profile = (
    dog_profile_builder
    .set_basic_info("Teddy", "Dog", 3)
    .add_medical_history("Neutered")
    .add_behavior_notes("Energetic")
    .add_vaccination_status("Parvo", date(2021, 2, 1))
    .build()
  )

  dog_factory = DogFactory()
  new_dog = dog_factory.create_animal(dog_profile)

  shelter.add_animal(new_dog)

  # when variables reference the same instance
  shelter2 = ShelterManagement()
  print(f"Same shelter instance? {shelter is shelter2}")

  for animal in shelter.list_animals():
    print(f"\nAnimal: {animal.profile.name}")
    print(f"Species: {animal.profile.species}")
    print(f"Sound: {animal.make_sound()}")
    print(f"Care instructions: {animal.get_care_instructions()}")

if __name__ == "__main__":
  main()