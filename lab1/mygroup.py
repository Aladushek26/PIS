groupmates = [
    {
        "name": "Павел",
        "surname": "Семеновых",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Мухамет",
        "surname": "Идрисов",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Анатолий",
        "surname": "Жабров",
        "exams": ["ПИС", "ИС", "МИС"],
        "marks": [5, 5, 5]
    }
]

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))

def filter_students_by_average(students, threshold):
    filtered = []
    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])
        if avg > threshold:
            filtered.append(student)
    return filtered

# Пример использования
threshold = float(input("Введите минимальный средний балл для фильтрации: "))
filtered_students = filter_students_by_average(groupmates, threshold)
print_students(filtered_students)

