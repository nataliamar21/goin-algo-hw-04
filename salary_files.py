from pathlib import Path
def total_salary(path):
    try:
        with open(Path(path), 'r', encoding='utf-8') as salary_file:
            lines = salary_file.readlines()
        total_salary = 0
        count = 0
        for line in lines:
            name, salary = line.strip().split(',')
            total_salary += int(salary)
            count += 1
        if count > 0:
            average_salary = total_salary / count
        else:
            average_salary = 0
        return total_salary, average_salary
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return 0, 0
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")