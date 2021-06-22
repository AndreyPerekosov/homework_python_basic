class User():
    def __init__(self, name, surname, mail, mobile_phone, password, *pets):
        self.name = name
        self.surname = surname
        self.mail = mail
        self.mobile_phone = mobile_phone
        self.__password = password
        self._pets = []
        for pet in pets:
            self.pets.append(pet)

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def pets(self):
        return self._pets

    @pets.setter
    def pets(self, pet):
        self.__iadd__(pet)

    def __iadd__(self, item):
        self._pets.append(item)
        return self

def t(*pets):
    data = []
    for pet in pets:
        data.append(pet)
    return data
print(t())