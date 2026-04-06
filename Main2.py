#Реализуйте простой менеджер задач:
# храните
#задачи в файле tasks.json, каждая задача содержит: ID
#выполнена);
#выполненной задачи, удаление задачи;
# при запуске загружайте существующие задачи из файла, если он есть;
# обеспечьте обработку ошибок при работе с JSON и файлом;
# добавьте подтверждение перед удалением задачи.
import json
import os

FILENAME = "tasks.json"

def load_tasks():
    try:
        if os.path.exists(FILENAME):
            with open(FILENAME, "r", encoding="utf-8") as f:
                return json.load(f)
    except json.JSONDecodeError:
        print("Ошибка: Файл поврежден!")
    except Exception as e:
        print(f"Ошибка загрузки: {e}")
    return []

def save_tasks(tasks):
    try:
        with open(FILENAME, "w", encoding="utf-8") as f:
            json.dump(tasks, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print(f"Ошибка сохранения: {e}")
        return False

def add_task(tasks):
    title = input("Название задачи: ")
    if not title:
        print("Название не может быть пустым!")
        return
    desc = input("Описание: ")
    
    new_id = 1
    if tasks:
        new_id = max(t["id"] for t in tasks) + 1
    
    tasks.append({
        "id": new_id,
        "title": title,
        "description": desc,
        "completed": False
    })
    save_tasks(tasks)
    print(f"Задача #{new_id} добавлена!")

def view_tasks(tasks):
    if not tasks:
        print("Список пуст.")
        return
    print(" Задачи ")
    for t in tasks:
        status = "[x]" if t["completed"] else "[ ]"
        print(f"{status} #{t['id']} {t['title']}")
        if t["description"]:
            print(f"    {t['description']}")


def complete_task(tasks):
    id_str = input("ID задачи для завершения: ")
    for t in tasks:
        if str(t["id"]) == id_str:
            t["completed"] = True
            save_tasks(tasks)
            print(f"Задача #{id_str} выполнена!")
            return
    print("Задача не найдена!")

def delete_task(tasks):
    id_str = input("ID задачи для удаления: ")
    for i, t in enumerate(tasks):
        if str(t["id"]) == id_str:
            confirm = input(f"Удалить '{t['title']}'? (да/нет): ")
            if confirm.lower() in ["да", "yes", "y"]:
                tasks.pop(i)
                save_tasks(tasks)
                print(f"Задача #{id_str} удалена!")
            else:
                print("Удаление отменено.")
            return
    print("Задача не найдена!")

def main():
    tasks = load_tasks()
    print(f"Загружено задач: {len(tasks)}\n")
    
    while True:
        print("1 - Добавить")
        print("2 - Показать")
        print("3 - Выполнить")
        print("4 - Удалить")
        print("5 - Выход")
        
        choice = input("Выбор: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break
        else:
            print("Неверный выбор!")
        print()

if __name__ == "__main__":
    main()