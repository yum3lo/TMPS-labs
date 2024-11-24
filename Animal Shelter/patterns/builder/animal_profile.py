from datetime import date

class AnimalProfile:
  def __init__(self):
    self.name = None
    self.species = None
    self.age = None
    self.medical_history = []
    self.behavior_notes = []
    self.special_needs = []
    self.medication = []
    self.vaccination_status = {}

class AnimalProfileBuilder:
  def __init__(self):
    self.profile = AnimalProfile()

  def set_basic_info(self, name: str, species: str, age: int):
    self.profile.name = name
    self.profile.species = species
    self.profile.age = age
    return self

  def add_medical_history(self, condition: str):
    self.profile.medical_history.append(condition)
    return self

  def add_medication(self, med: str, schedule: str):
    self.profile.medication.append(f"{med} {schedule}")
    return self

  def add_behavior_notes(self, note: str):
    self.profile.behavior_notes.append(note)
    return self

  def add_special_needs(self, need: str):
    self.profile.special_needs.append(need)
    return self

  def add_vaccination_status(self, vaccine: str, date_administered: date):
    self.profile.vaccination_status[vaccine] = date_administered
    return self
  
  def update_medical_history(self, condition: str):
    self.profile.add_medical_history(condition)
    self.notify_observers(f"Medical update: {condition}")

  def update_behavior_notes(self, note: str):
    self.profile.add_behavior_notes(note)
    self.notify_observers(f"Behavior update: {note}")

  def update_special_needs(self, need: str):
    self.profile.add_special_needs(need)
    self.notify_observers(f"Special needs update: {need}")

  def build(self):
    return self.profile