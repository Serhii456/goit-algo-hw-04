from pathlib import Path

def total_salary(path):
   try:
      with open(path, encoding='utf-8') as file:
         total_salary = 0
         count_developers = 0
         for line in file:
            developer_data = line.strip().split(',')
            if len(developer_data) != 2:
               print (f"Невірний формат даних у рядку: {line}")
               return [0,0]
            developer_name, salary_str = developer_data
            salary = float(salary_str)
            total_salary += salary
            count_developers += 1
         average_salary = total_salary / count_developers
         return total_salary, average_salary
   except FileNotFoundError:
      print (f"Файл не знайдено: {path}")
      return [0,0]
   except ValueError as e:
      print (f"Помилка при обробці даних: {e}")
      return [0,0]
       


total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")