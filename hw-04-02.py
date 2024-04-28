def get_cats_info(path):
  try:
    with open(path, encoding='utf-8') as file:
      cats_info = []
      for line in file:
        cat_data = line.strip().split(',')
        if len(cat_data) != 3:
          print (f"Неправильний формат даних у рядку: {line}")
        cat_id, cat_name, cat_age = cat_data
        cat_info = {
          "id": cat_id,
          "name": cat_name,
          "age": int(cat_age)
        }
        cats_info.append(cat_info)
  except FileNotFoundError:
    print (f"Файл не знайдено: {path}")
    return [{"id":"", "name": "", "age": "" }]
  except ValueError as e:
    print (f"Помилка при обробці даних: {e}")

  return cats_info

cats_info = get_cats_info("cats_file.txt")
print(cats_info)
