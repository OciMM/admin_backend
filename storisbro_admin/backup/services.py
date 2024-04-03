import os
import shutil
import json
from django.http import FileResponse
from zipfile import ZipFile

from notifications.models import AutoNotificationModel

# создание zip файла
# позже здесь нужно добавить путь, который будет сервере
def create_zip_of_django_project(source_folder, zip_filename='django_project.zip'):
    try:
        if not os.path.exists(source_folder):
            raise FileNotFoundError(f"Source folder '{source_folder}' not found.")

        # Создаем архив с кодом проекта
        shutil.make_archive(zip_filename.replace('.zip', ''), 'zip', source_folder)

        print(f"Код проекта успешно сохранен в {zip_filename}")

        with open(zip_filename, 'rb') as zip_file:
            response = FileResponse(zip_file)

        os.remove(zip_filename)  # Удаляем временный файл архива
        return response
    except FileNotFoundError as e:
        print(f"Произошла ошибка: {e}")
    except Exception as e:
        print(f"Произошла неожиданная ошибка: {e}")


# def download_script(zip_file_path):
#     zip_file = open(zip_file_path, 'rb')

#     # Создаем и возвращаем HTTP-ответ с файлом
#     response = FileResponse(zip_file, as_attachment=True, filename=os.path.basename(zip_file_path))
#     return response

def download_db(folder_path):
    # Получаем список файлов в папке
    files = os.listdir(folder_path)

    # Сортируем файлы по времени создания (по умолчанию, сначала старые)
    files.sort(key=lambda x: os.path.getctime(os.path.join(folder_path, x)))

    # Выбираем последний файл
    latest_file = files[-1]

    # Открываем последний zip-файл, не закрывая его
    zip_file_path = os.path.join(folder_path, latest_file)
    zip_file = open(zip_file_path, 'rb')

    # Создаем и возвращаем HTTP-ответ с файлом
    response = FileResponse(zip_file, as_attachment=True, filename=latest_file)

    # Не закрываем файл здесь, FileResponse сама закроет его после отправки

    return response