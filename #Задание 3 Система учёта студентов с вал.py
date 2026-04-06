#Задание 3 Система учёта студентов с валидацией
#Разработайте программу учёта студентов:
# храните данные о студентах в файле students.json: ID (автогенерация),
#имя, возраст, группа, оценки (список);
# реализуйте интерфейс командной строки для: добавления студента (с
#валидацией возраста > 16 и оценок в диапазоне 2–5), просмотра списка
#студентов, поиска по имени/группе, расчёта среднего балла для студента;
# при запуске загружайте данные из файла, если он существует;
# сохраняйте изменения в файл после каждой операции;
# обрабатывайте все возможные ошибки ввода и файловые ошибки;
# добавьте экспорт данных в CSV‑формат.
import json
import os
import csv

FILE = "students.json"
CSV_FILE = "students.csv"

def load_students():
    try:
        if os.path.exists(FILE):
            with open(FILE, "r", encoding="utf-8") as f:
                return json.load(f)
    except:
        print("Не удалось прочитать файл")
    return []

def save_students(students):
    try:
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(students, f, ensure_ascii=False, indent=4)
        return True
    except:
        print("Не удалось сохранить файл")
        return False

def input_age():
    while True:
        try:
            age = int(input("Возраст: "))
            if age > 16:
                return age
            print("Возраст должен быть больше 16!")
        except:
            print("Введите число!")

def input_grades():
    grades = []
    print("Вводите оценки по одной (2-5). Пустая строка - готово:")
    while True:
        g = input("Оценка: ")
        if g == "":
            break
        try:
            grade = int(g)
            if 2 <= grade <= 5:
                grades.append(grade)
            else:
                print("Оценка должна быть от 2 до 5!")
        except:
            print("Введите число!")
    return grades

def add_student(students):
    name = input("Имя: ")
    if name == "":
        print("Имя не может быть пустым!")
        return
    
    age = input_age()
    group = input("Группа: ")
    grades = input_grades()
    
    new_id = 1
    if students:
        new_id = max(s["id"] for s in students) + 1
    
    student = {
        "id": new_id,
        "name": name,
        "age": age,
        "group": group,
        "grades": grades
    }
    
    students.append(student)
    save_students(students)
    print(f"Студент #{new_id} добавлен!")

def view_students(students):
    if not students:
        print("Список пуст")
        return
    
    print("Список студентов")
    for s in students:
        avg = calc_average(s["grades"])
        print(f"ID: {s['id']} | {s['name']} | {s['age']} лет | Группа: {s['group']} | Средний балл: {avg}")


def calc_average(grades):
    if not grades:
        return 0
    return round(sum(grades) / len(grades), 2)

def search_student(students):
    print("1 - По имени")
    print("2 - По группе")
    choice = input("Выбор: ")
    
    query = input("Введите запрос: ")
    found = []
    
    for s in students:
        if choice == "1" and query.lower() in s["name"].lower():
            found.append(s)
        elif choice == "2" and query.lower() in s["group"].lower():
            found.append(s)
    
    if not found:
        print("Ничего не найдено!")
        return
    
    print("Результаты:")
    for s in found:
        avg = calc_average(s["grades"])
        print(f"ID: {s['id']} | {s['name']} | Группа: {s['group']} | Средний балл: {avg}")

def show_average(students):
    student_id = input("ID студента: ")
    
    for s in students:
        if str(s["id"]) == student_id:
            avg = calc_average(s["grades"])
            print(f"Средний балл {s['name']}: {avg}")
            return
    print("Студент не найден!")

def export_csv(students):
    try:
        with open(CSV_FILE, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Имя", "Возраст", "Группа", "Оценки", "Средний балл"])
            for s in students:
                avg = calc_average(s["grades"])
                grades_str = ", ".join(map(str, s["grades"]))
                writer.writerow([s["id"], s["name"], s["age"], s["group"], grades_str, avg])
        print(f"Файл {CSV_FILE} создан!")
    except Exception as e:
        print(f"Ошибка: {e}")

def main():
    students = load_students()
    print(f"Загружено: {len(students)} студентов\n")
    
    while True:
        print("1 - Добавить студента")
        print("2 - Показать всех")
        print("3 - Поиск")
        print("4 - Средний балл")
        print("5 - Экспорт в CSV")
        print("6 - Выход")
        
        choice = input("Выбор: ")
        
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            show_average(students)
        elif choice == "5":
            export_csv(students)
        elif choice == "6":
            break
        else:
            print("Неверный выбор!")
        print()

if __name__ == "__main__":
    main()