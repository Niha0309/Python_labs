#classes
class Keyboard:
    def definition(self):
        print("keyboard is an input device")

    def number_of_keys(self):
        print('there are 101 keys')


my_keyboard = Keyboard()
my_keyboard.definition()
my_keyboard.brand = "logitech"
print(my_keyboard.brand)

new_keyboard = Keyboard()
new_keyboard.definition()
new_keyboard.brand = "dell"
print(new_keyboard.brand)
