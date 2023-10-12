#INTRO TO IT 2nd COURSE
# Задача 7: Факториал на месте!
# Рассчитай факториал введенного числа.
def factorial(число):
    return 1 if число == 0 else число * factorial(число-1)
число = 5
print(f"factorial {число} равен {factorial(число)}")
