#constructor
class Keyboard:
    def __init__(self, language, connection):
        self.language = language
        self.connection = connection

    def definition(self):
        print("keyboard is an input device")

    def number_of_keys(self):
        print('there are 101 keys')


my_keyboard = Keyboard('english', 'wireless')
print(my_keyboard.connection)

class AboutMe:
    def __init__(self, name, address, occupation):
        self.name = name
        self.address = address
        self.occupation = occupation

    def talk(self):
        print(f"My name is {self.name}. I am from {self.address}. "
              f"And I am a {self.occupation}")


Niha = AboutMe('Fahima Lokman Niha', 'Bangladesh', 'student')
Niha.talk()
