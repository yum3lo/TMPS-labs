# Laboratory Work 3: Behavioral Design Patterns
## Author: Cucoș Maria
----

## Task
By extending your project, implement at least 1 behavioral design pattern in your project:
* The implemented design pattern should help to perform the tasks involved in your system.
* The behavioral DPs can be integrated into your functionalities alongside the structural ones.
* There should only be one client for the whole system.

## Used Design Patterns:
* Observer

## Implementation

## Observer Pattern
Observer is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing. [1]
In this case, when the `Animal` object changes its state (ex: medical or behavioral updates), all registered observers (the staff, the vet and the owner) are automatically notified.

### The observer (`AnimalObserver` and its subclasses)
The `AnimalObserver` is an abstract class that defines the update method, which the specific observers `StaffObserver`, `VetObserver`, `OwnerObserver` implement. Each observer is responsible for formatting the message according to its role (staff, vet, owner) and then notifying the `NotificationManager` to send the message via email or SMS using the Adapter pattern from the previous laboratory. 

```python
def __init__(self, notification_manager: NotificationManager, role: str):
    self.notification_manager = notification_manager
    self.role = role
```

The `StaffObserver` is responsible for notifying the shelter staff when an update happens. It includes general animal details and care instructions.

```python
def update(self, animal: "Animal", message: str):
    full_message = (
        f"Name: {animal.profile.name}\n"
        f"Species: {animal.profile.species}\n"
        f"Update: {message}\n"
        f"Care Instructions: {animal.get_care_instructions()}"
    )
    self.notification_manager.notify(self.role, full_message)
```

The `VetObserver` sends detailed medical information to the vet, including medications and medical history.

```python
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
```

The `OwnerObserver` sends a simple update to the animal's owner, notifying them of changes.

```python
def update(self, animal: "Animal", message: str):
    full_message = (
        f"Name: {animal.profile.name}\n"
        f"Update: {message}\n"
    )
    self.notification_manager.notify(self.role, full_message)
```

### The observed (`ObservedAnimal` and its subclasses)
The `ObservedAnimal` class and its subclasses `ObservedDog` and `ObservedCat` are responsible for notifying all known observers whenever the state of an animal changes.

The `ObservedAnimal` class extends the `Animal` class and adds the functionality for the Observer pattern. Moreover, it maintains a list of observers and notifies them when there is a change in the animal’s state.

```python
def add_observer(self, observer: AnimalObserver):
    if observer not in self._observers:
      self._observers.append(observer)

def remove_observer(self, observer: AnimalObserver):
    self._observers.remove(observer)

def notify_observers(self, message: str):
    for observer in self._observers:
        observer.update(self, message)
```

The subclasses are specific implementations for `Dog` and `Cat`. They inherit the observer behavior from `ObservedAnimal` and use it with the specific behavior of the `Dog` and `Cat` classes. Both `ObservedDog` and `ObservedCat` have the ability to add/remove observers and notify them about any changes in the animal's state.

## Conclusions

In this project, the Observer Pattern was used to notify different shelter parties (staff, vet, and owner) about updates related to the observed animals. Each observer is registered to listen for changes, and when an update occurs, the relevant observers are notified and receive the appropriate formatted messages. The `NotificationManager` acts as the subject, managing the list of observers and notifying them when necessary. Also it is easy to link the Observed thing (the animal) and the Observers (staff, vet, and owner). This makes it easy to add or remove observers, and the observers only need to know about the changes in the animal, not the internal implementation details.

This pattern provides flexibility, as new observers can easily be added without modifying existing code.

## Bibliography
[1] [Observer](https://refactoring.guru/design-patterns/observer)