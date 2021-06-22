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
            self.init_user(pet)

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
        self.init_user(item)
        return self

    def init_user(self, pet):
        pet.user = self


class Pet():
    def __init__(self, name, kind, birth_date):
        self.name = name
        self.kind = kind
        self.birth_date = birth_date
        self.user = None


p_1 = Pet('tommy', 'cat', '03.06.18')
p_2 = Pet('ho', 'dog', '03.06.18')
u_1 = User('John', 'Smith', 'j@mail.com', '123', 'qwert', p_1, p_2)
p_3 = Pet('jacky', 'cat', '03.06.18')
p_4 = Pet('bo', 'dog', '03.06.18')
u_2 = User('Tom', 'Sawyer', 't@mail.com', '123', 'qwert', p_3)
u_2.pets = p_4
