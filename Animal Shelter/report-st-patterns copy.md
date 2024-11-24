# Laboratory Work 2: Structural Design Patterns
## Author: Cucoș Maria
----

## Task
By extending your project, implement at least 3 structural design patterns in your project:
* The implemented design pattern should help to perform the tasks involved in your system.
* The object creation mechanisms/patterns can now be buried into the functionalities instead of using them into the client.
* There should only be one client for the whole system.

## Used Design Patterns:
* Adapter
* Decorator
* Facade

## Implementation

### Adapter Pattern (`NotificationAdapter`)
Adapter is a structural design pattern that allows objects with incompatible interfaces to collaborate. [1]
I used the Adapter pattern to send notifications via Email through the `EmailNotification` class or SMS through the `SMSNotification` class. Both of the classes implement the `NotificationSystem` interface. The abstract base `NotificationAdapter` wraps 2 notification systems and adapts them to the main interface. It connects the facade with any chosen notification system and makes it easy to add other types of notifications, without having to modify the existing code. 

```python
def notify(self, recipient: str, message: str):
    self.notification_system.send_notification(recipient, message)
```

Here is how I called it in the facade:

```python
self.notification_adapter.notify("staff@shelter.com", message)
```

### Decorator Pattern (`AnimalDecorator`)
Decorator is a structural design pattern that lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors. [2]
This pattern was used in this project to add extra behaviour to the animal care instructions without having to modify the base `Animal` classes. The `AnimalDecorator` abstract class wraps an `Animal` object. `MedicalCareDecorator` adds the medication name and its "to be taken" schedule to an animal's care instructions.

```python
def get_care_instructions(self):
    base_instructions = super().get_care_instructions()
    return f"{base_instructions}, Give {self.medication} {self.schedule}"
```

Finally, the `SpecialNeedsDecorator` adds other extra care needs for the animal's specific requirement.

```python
def get_care_instructions(self):
    base_instructions = super().get_care_instructions()
    return f"{base_instructions}, {self.need}"
```

In the facade it gets the medication name and schedule and the special needs, adding it to the animal.

```python
for med in medication:
    med_name = med.get("name")
    med_schedule = med.get("schedule")
    animal = MedicalCareDecorator(animal, med_name, med_schedule)

for need in special_needs:
    animal = SpecialNeedsDecorator(animal, need)
```

### Facade (`ShelterFacade`)
Facade is a structural design pattern that provides a simplified interface to a library, a framework, or any other complex set of classes. [3]
In my project this pattern provides a simple interface for adding animals to the shelter and sending notifications about it. It helps manage the details and and makes it easy to add new animals with categorized information, like medical history, behavior notes, special needs, medication details, etc.
`ShelterFacade` intializes the shelter management system, from the previous laboratory using the Singleton creational pattern, and a notification adapter, from the Adapter structural pattern.

```python
self.shelter = ShelterManagement()
self.notification_adapter = NotificationAdapter(notification_system)
```
It has an `add_animal` method that creates an animal using the Builder pattern from the previous laboratory. Then it adds multiple elements to the animal's profile.

```python
for history in medical_history:
    animal_profile.add_medical_history(history)
for note in behavior_notes:
    animal_profile.add_behavior_notes(note)
for need in special_needs:
    animal_profile.add_special_needs(need)
for vaccine, date in vaccination_status.items():
    animal_profile.add_vaccination_status(vaccine, date)
```

Based on the species of the animal, the facade uses the right `AnimalFactory`, Factory pattern from the previous laboratory, to create a `Cat` or a `Dog`. Then it applies `MedicalCareDecorator` and `SpecialNeedsDecorator` if the animal has some specifications. After creating the animal, the facade sends a notification to the shelter staff containing information about the animal's special needs or medications.

### Main Flow
In `main.py` the shelter facade adds new animals with their specific information details and care needs. 

```python
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
```

This proves how the structural patterns used - `Adapter`, `Decorator` and `Facade` - work together to simplify the main flow of the application. The only client in this project is the `main.py` file that interacts with the facade and can request things from it. Here is an example of the output:

```
Email sent to staff@shelter.com: 
Name: Mia
Species: Cat
Medical History: Vaccinated, Needs daily medication
Vaccinations:
  - Rabies: 2021-02-01
  - FVRCP: 2023-06-12
Behavior Notes: Friendly
Care Instructions: Feed three times, Give fresh water, Clean litter box, Give 
Painkillers every 12 hours, Give Antibiotics every 24 hours, Grain-free diet 
```

## Conclusions

This project uses 3 structural patterns: Adapter, Decorator and Facade. The Adapter abstracts the notification system, handling 2 messaging systems. Decorator extends the care instructions with special needs and medications, making the system more flexible and easy to extend with more options. Finally, the Facade simplifies the process of adding animals, making use of the Builder, Singleton and Factory patterns from the previous lab. It also hides the complex parts from the client, keeping the main file cleaner and more readable

## Bibliography
[1] [Adapter](https://refactoring.guru/design-patterns/adapter)
[2] [Decorator](https://refactoring.guru/design-patterns/decorator)
[3] [Facade](https://refactoring.guru/design-patterns/facade)
