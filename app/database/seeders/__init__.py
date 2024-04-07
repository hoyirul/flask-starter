import os
from common.string import String
import importlib

classes = []

try:
    # Tentukan path ke folder yang ingin Anda baca
    folder_path = 'app/database/seeders/'

    # Mendapatkan daftar nama file di dalam folder
    file_names = os.listdir(folder_path)

    # Menyaring nama file yang berakhiran dengan ".py" dan bukan "__init__.py"
    py_files = [file_name for file_name in file_names if file_name.endswith('.py') and not file_name.startswith('__init__')]

    # Menampilkan nama-nama file .py yang valid
    for file_name in py_files:
        module_name, class_name = String(file_name).dbfile_to_class_name()
        # Lakukan impor dinamis untuk setiap modul
        module = importlib.import_module(f'app.database.seeders.{module_name}')
        # Tambahkan impor untuk kelas yang akan digunakan
        globals()[class_name] = getattr(module, class_name)
        classes.append(getattr(module, class_name))

except FileNotFoundError:
    print("Folder tidak ditemukan")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")

class DatabaseSeeder:
    def __init__(self):
        pass

    def seed(self):
        for class_name in classes:
            class_name().run()