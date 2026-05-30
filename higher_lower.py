import os
import time
import sys
import keyboard
import random

def show_logo():
    print("""
esc для пропуска
разработчики:
██╗░░██╗███████╗████████╗░░░░░░░░░██╗░░██╗░█████╗░████████╗
██║░██╔╝██╔════╝╚══██╔══╝░░░░░░░░░██║░██╔╝██╔══██╗╚══██╔══╝
█████╔╝░█████╗░░░░░██║░░░░░░░░░░░░█████╔╝░███████║░░░██║░░░
██╔═██╗░██╔══╝░░░░░██║░░░░░░░░░░░░██╔═██╗░██╔══██║░░░██║░░░
██║░░██╗███████╗░░░██║░░░███████╗░██║░░██╗██║░░██║░░░██║░░░
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░
""")

def clear_screen_with_logo():
    os.system("cls")  
    show_logo()

show_logo()

spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧"]
skip_loading = False

for _ in range(15):
    for s in spinner:
        if keyboard.is_pressed('esc'):
            skip_loading = True
            break
        
        sys.stdout.write(f"\r {s} Загрузка {s} ")
        sys.stdout.flush()
        time.sleep(0.05)
        
    if skip_loading: 
        break
def player():
    score = 0
    random_int_old = random.randint(1, 10)

    while True:
        random_int_nov = random.randint(1, 10)
        
        print("\n" + "="*30)
        print(f"score: {score} | Текущее число: {random_int_old}")

        player_input = input("Какое число будет следующим? (выше, ниже, равняется) \n/// ").lower().strip()
        
        print(f"Следующее число было: {random_int_nov}")
        
        if player_input == "равняется":
            if random_int_nov == random_int_old:
                score += 2
                print("Вы угадали! +2 очка")
            else:
                score -= 1
                print("Вы не угадали... -1 очко")
                
        elif player_input == "ниже":
            if random_int_nov < random_int_old:
                score += 1
                print("Вы угадали! +1 очко")
            else:
                score -= 1
                print("Вы не угадали... -1 очко")
                
        elif player_input == "выше":
            if random_int_nov > random_int_old:
                score += 1
                print("Вы угадали! +1 очко")
            else:
                score -= 1
                print("Вы не угадали... -1 очко")
                
        else:
            print("Неизвестная команда! (выше, ниже или равняется)")
            continue
        random_int_old = random_int_nov
        time.sleep(1.5)

def computer():
    comp_score = 0
    rules = ["выше", "ниже", "равняется", "выше", "ниже","выше", "ниже"]
    while True:
        try:
            random_int_old = int(input("Введите стартовое число (от 1 до 10): \n/// "))
            if 1 <= random_int_old <= 10:
                break
            print("Пожалуйста, введите число именно от 1 до 10!")
        except ValueError:
            print("Это не число! Введите цифру.")

    while True:
        bot_guess = random.choice(rules)
        
        print("\n" + "="*30)
        print(f"Счет бота: {comp_score} | Текущее число: {random_int_old}")
        print(f"Бот прогнозирует, что ваше СЛЕДУЮЩЕЕ число будет: {bot_guess.upper()}")
        
        while True:
            try:
                random_int_nov = int(input("Введите следующее число (от 1 до 10) или '0' для выхода: \n/// "))
                if random_int_nov == 0:
                    print("Выход в главное меню...")
                    return
                if 1 <= random_int_nov <= 10:
                    break
                print("Число должно быть от 1 до 10!")
            except ValueError:
                print("Пожалуйста, введите корректное число.")

        print(f"\nВы ввели: {random_int_nov} (Прогноз бота был: {bot_guess})")

        if bot_guess == "равняется":
            if random_int_nov == random_int_old:
                comp_score += 2
                print("Я угадал равенство! +2 очка")
            else:
                comp_score -= 1
                print("Я не угадал -1 очко")
                
        elif bot_guess == "ниже":
            if random_int_nov < random_int_old:
                comp_score += 1
                print("Я угадал! +1 очко")
            else:
                comp_score -= 1
                print("Я не угадал -1 очко")
                
        elif bot_guess == "выше":
            if random_int_nov > random_int_old:
                comp_score += 1
                print("Я угадал! +1 очко")
            else:
                comp_score -= 1
                print("Я не угадал-1 очко")
        random_int_old = random_int_nov
        time.sleep(1.5)


while True:
    hi = input("привет! это игра ВЫШЕ, ниже кто будет угадовать? (я, ты) \n///  ").lower().strip()
    if hi == "я":
        player()
    if hi == "ты":
        computer()
    else:
        print("что?")