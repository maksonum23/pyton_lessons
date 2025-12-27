import os
import platform

print("--- ЗАПУСК ПРОВЕРКИ ---")
print("Система:", platform.system(), platform.release())
print("Пользователь:", os.getlogin())
print("Папка запуска:", os.getcwd())
print("--- УСПЕХ ---")