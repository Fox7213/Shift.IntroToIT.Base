#INTRO TO IT 2nd COURSE
# Задача 6: Гласные в высоте!
# Посчитай количество гласных букв в строке.
def podschet_glasn(строка):
    return sum(1 for символ in строка if символ.lower() in "аеёиоуыэюя")
строка = "Привет, мир!"
print(f"В '{строка}' {podschet_glasn(строка)} гласных")
