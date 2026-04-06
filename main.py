#Задание 1 Базовый файловый менеджер
def write_to_file(filename, text):
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(text + "\n")
        return True
    except PermissionError:
        print("Ошибка: Нет прав доступа к файлу!")
        return False
    except Exception as e:
        print(f"Ошибка записи: {e}")
        return False

def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            print("Содержимое файла:")
            print(content)
    except FileNotFoundError:
        print("Ошибка: Файл не найден!")
    except PermissionError:
        print("Ошибка: Нет прав доступа!")
    except UnicodeDecodeError:
        print("Ошибка: Проблема с кодировкой!")
    except Exception as e:
        print(f"Ошибка чтения: {e}")

filename = input("Введите имя файла: ")

while True:
    text = input("Введите строку (или 'exit' для выхода): ")
    
    if text.lower() == 'exit':
        break
    
    if not text:
        continue

    if write_to_file(filename, text):
        read_file(filename)