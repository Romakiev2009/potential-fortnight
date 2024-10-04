import random
import colorama
from colorama import Fore, Style

# Ініціалізація colorama
colorama.init()

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print(Fore.CYAN + "Вітаємо у грі 'Вгадай число'!")
    print("Я загадав число від 1 до 100. Спробуй вгадати його!" + Style.RESET_ALL)

    while True:
        try:
            user_guess = int(input(Fore.YELLOW + "Введіть ваше число: " + Style.RESET_ALL))
            attempts += 1

            if user_guess < number_to_guess:
                print(Fore.RED + "Загадане число більше. Спробуйте ще!" + Style.RESET_ALL)
            elif user_guess > number_to_guess:
                print(Fore.RED + "Загадане число менше. Спробуйте ще!" + Style.RESET_ALL)
            else:
                print(Fore.GREEN + f"Вітаємо! Ви вгадали число {number_to_guess} за {attempts} спроб!" + Style.RESET_ALL)
                break

        except ValueError:
            print(Fore.RED + "Будь ласка, введіть дійсне число." + Style.RESET_ALL)

# Виклик функції
guess_the_number()

# Деініціалізація colorama
colorama.deinit()
