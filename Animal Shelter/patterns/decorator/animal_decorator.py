from models.animal import Animal

class AnimalDecorator(Animal):
  def __init__(self, animal: Animal):
    self.animal = animal
    super().__init__(animal.profile)

  def make_sound(self):
    return self.animal.make_sound()

  def get_care_instructions(self):
    return self.animal.get_care_instructions()

class MedicalCareDecorator(AnimalDecorator):
  def __init__(self, animal: Animal, medication: str, schedule: str):
    super().__init__(animal)
    self.medication = medication
    self.schedule = schedule
    self.animal.profile.medication.append(f"{self.medication} {self.schedule}")

  def get_care_instructions(self):
    base_instructions = super().get_care_instructions()
    return f"{base_instructions}, Give {self.medication} {self.schedule}"

class SpecialNeedsDecorator(AnimalDecorator):
  def __init__(self, animal: Animal, need: str):
    super().__init__(animal)
    self.need = need

  def get_care_instructions(self):
    base_instructions = super().get_care_instructions()
    return f"{base_instructions}, {self.need}"