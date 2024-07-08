from pathlib import Path
def get_cats_info(path):
    cats_info = []
    try:
        with open(Path(path), 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }
                cats_info.append(cat_info)
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return cats_info

# Приклад використання функції
cats_info = get_cats_info("cats_file.txt")
print(cats_info)