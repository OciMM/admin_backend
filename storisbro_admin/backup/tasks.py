from celery import shared_task

import os
import shutil
from datetime import datetime


@shared_task(bind=True)
def backup_database(self):
     # Путь к файлу db.sqlite3
    db_path = os.path.join(os.getcwd(), 'db.sqlite3')

    # Путь для сохранения архива
    backup_path = os.path.join(os.getcwd(), 'backups_zip')
    os.makedirs(backup_path, exist_ok=True)

    # Имя файла архива с датой
    zip_filename = f"backup_db_{datetime.now().strftime('%Y%m%d')}.zip"
    zip_path = os.path.join(backup_path, zip_filename)

    # Копируем db.sqlite3 во временный файл
    tmp_db_path = os.path.join(backup_path, 'tmp_db.sqlite3')
    shutil.copy2(db_path, tmp_db_path)

    # Архивируем файл
    shutil.make_archive(zip_path[:-4], 'zip', backup_path, 'tmp_db.sqlite3')

    # Удаляем временный файл
    os.remove(tmp_db_path)