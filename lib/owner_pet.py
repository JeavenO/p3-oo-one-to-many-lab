class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # stores all Pet instances

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type")
        self.pet_type = pet_type

        self.owner = None
        if owner:
            self.owner = owner
            owner.add_pet(self)  # automatically add pet to owner's list

        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # private list to track owned pets

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Only Pet instances can be added")
        if pet not in self._pets:
            self._pets.append(pet)
            pet.owner = self

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)

alice = Owner("Alice")
fido = Pet("Fido", "dog")
whiskers = Pet("Whiskers", "cat", owner=alice)

alice.add_pet(fido)

print([pet.name for pet in alice.get_sorted_pets()])
# => ['Fido', 'Whiskers']

print([pet.name for pet in Pet.all])
# => ['Fido', 'Whiskers']
