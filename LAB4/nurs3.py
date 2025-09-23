# 1) Тізімді кері шығару
lst = [1, 2, 3, 4, 5]
print(lst[::-1])

# 2) Модулі бойынша кему ретімен сұрыптау
def list_sort(lst):
    return sorted(lst, key=abs, reverse=True)
print(list_sort([3, -7, 2, -10, 5]))

# 3) Бірінші және соңғы элементтерді ауыстыру
def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
print(change([10, 20, 30, 40]))
