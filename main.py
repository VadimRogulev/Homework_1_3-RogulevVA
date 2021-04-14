"""
3. Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 — получаем «5 процентов»,
задаем число 2 — получаем «2 процента». Вывести все склонения для проверки.
"""

percent = ' процент'

# while True:
#     user_number = int(input("Введите любое число: "))

# Вывести все склонения для проверки
for user_number in range(20):
    if user_number == 0 or user_number // 10 == 1 or user_number % 10 == 0 or 4 < (user_number % 10) <= 9:
        declination = 'ов'
    elif user_number % 10 == 1:
        declination = ''
    elif 1 < (user_number % 10) < 5:
        declination = 'а'
    print(str(user_number) + percent + declination)
