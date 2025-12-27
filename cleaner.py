import os
import shutil

# 1. Указываем папку, где будем наводить порядок
# (точка означает "текущая папка", значит ищем папку chaos рядом со скриптом)
folder_path = "chaos"

print(f"--- Начинаю уборку в папке: {folder_path} ---")

# 2. Получаем список всех файлов в этой папке
files = os.listdir(folder_path)

for filename in files:
    # Собираем полный путь к файлу (например: chaos/photo.png)
    full_path = os.path.join(folder_path, filename)

    # Если это папка - пропускаем её, не трогаем
    if os.path.isdir(full_path):
        continue

    # 3. Определяем расширение файла (все, что после точки)
    # os.path.splitext делит имя на ("photo", ".png")
    _, extension = os.path.splitext(filename)
    
    # 4. Решаем, куда класть (простая логика)
    target_folder = "Raznoe"  # Если не знаем, что это - кидаем в "Разное"
    
    if extension in ['.jpg', '.png', '.jpeg', '.gif']:
        target_folder = "Images"
    elif extension in ['.pdf', '.txt', '.docx', '.doc']:
        target_folder = "Documents"
    elif extension in ['.exe', '.deb', '.zip']:
        target_folder = "Installers"

    # 5. Создаем целевую папку, если её еще нет
    # (например chaos/Images)
    target_path = os.path.join(folder_path, target_folder)
    os.makedirs(target_path, exist_ok=True)

    # 6. Перемещаем файл
    # Откуда (full_path) -> Куда (target_path + имя файла)
    shutil.move(full_path, os.path.join(target_path, filename))
    
    print(f"Перенес: {filename} -> {target_folder}")

print("--- Уборка завершена ---")