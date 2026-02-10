import multiprocessing
import os
import time
from multiprocessing import Pool


def process_file(file_path):

    #Функция для обработки файла: подсчитывает количество строк.

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            line_count = sum(1 for _ in file)
        print(f"Файл {file_path} обработан, строк: {line_count}")
        return file_path, line_count
    except FileNotFoundError:
        print(f"Файл {file_path} не найден")
        return (file_path, 0)
    except Exception as e:
        print(f"Ошибка при обработке файла {file_path}: {e}")
        return (file_path, 0)


def main():
    # Создаем тестовые файлы
    sample_data = {
        "file1.txt": "Строка 1\nСтрока 2\nСтрока 3",
        "file2.txt": "Строка 1\nСтрока 2\nСтрока 3\nСтрока 4",
        "file3.txt": "Строка 1\nСтрока 2\nСтрока 3\nСтрока 4\nСтрока 5"
    }

    # Записываем тестовые данные в файлы
    for file_name, content in sample_data.items():
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Создан тестовый файл: {file_name}")

    # Список путей к файлам для обработки
    file_paths = ["file1.txt", "file2.txt", "file3.txt"]
    # Используем Pool для параллельной обработки
    with Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(process_file, file_paths)

    # Выводим результаты
    print("\nРезультаты обработки файлов:")
    for file_path, line_count in results:
        print(f"{file_path}: {line_count} строк")

    # Очищаем тестовые файлы
    print("\nОчистка тестовых файлов...")
    time.sleep(1)
    for file_path in file_paths:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Удален файл: {file_path}")


if __name__ == "__main__":
    main()