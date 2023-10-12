#INTRO TO IT 2nd COURSE
# Задача 10: Квадраты на улице!
# Создай список, содержащий квадраты чисел от 0 до введенного числа.
def generat_cvadratov(число):
    return [x**2 for x in range(число)]
число = 5
print(f"{число} первых квадратов: {generat_cvadratov(число)}")
