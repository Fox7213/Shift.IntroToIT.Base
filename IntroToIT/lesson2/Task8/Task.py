#INTRO TO IT 2nd COURSE
# Задача 8: Слова, слова, слова!
# Узнай количество слов в предложении.
def podshet_slov(строка):
    return len(строка.split())
строка = "Python прекрасен!"
print(f"В '{строка}' {podshet_slov(строка)} слов")
