from abc import ABC, abstractmethod

# single responsibility principle
class Cat:
  def __init__(self, name, breed, id_number):
    self.name = name
    self.breed = breed
    self.id_number = id_number

class ShelterCatalog:
  def __init__(self):
    self.cats = []

  def add_cat(self, cat):
    self.cats.append(cat)

  def remove_cat(self, id_number):
    self.cats = [cat for cat in self.cats if cat.id_number != id_number]

  def get_cat(self, id_number):
    return next((cat for cat in self.cats if cat.id_number == id_number), None)

# open/closed principle
class SearchStrategy(ABC):
  @abstractmethod
  def search(self, catalog, query):
    pass

class NameSearch(SearchStrategy):
  def search(self, catalog, query):
    return [cat for cat in catalog.cats if query.lower() in cat.name.lower()]

class BreedSearch(SearchStrategy):
  def search(self, catalog, query):
    return [cat for cat in catalog.cats if query.lower() in cat.breed.lower()]

class CatalogSearch:
  def __init__(self, strategy):
    self.strategy = strategy

  def search(self, catalog, query):
    return self.strategy.search(catalog, query)


if __name__ == "__main__":
  catalog = ShelterCatalog()
  catalog.add_cat(Cat("Busea", "Siamese", "B001"))
  catalog.add_cat(Cat("Mia", "British Shorthair", "M001"))

  name_search = CatalogSearch(NameSearch())
  breed_search = CatalogSearch(BreedSearch())

  print("Searching for 'busea' in names:")
  for cat in name_search.search(catalog, "busea"):
    print(f"- {cat.name} ({cat.breed})")

  print("\nSearching for 'british shorthair' in breeds:")
  for cat in breed_search.search(catalog, "british shorthair"):
    print(f"- {cat.name} ({cat.breed})")