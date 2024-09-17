#function exceptipn
try:
    celsius = input('Tempreture in clesius ')
    celsius = int(celsius)
    farhrenhiet = (celsius * (9 / 5)) + 32
    print(farhrenhiet)
    print(f"F toc ratio(F/C): {farhrenhiet/celsius}")
except ValueError:
    print('Invalid input ')
except ZeroDivisionError:
    print('Celsius cannot be 0')