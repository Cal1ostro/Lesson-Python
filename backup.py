# encoding = utf8
import os
import time

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['C:\\Keys']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.

# 2. Резервыне копии должны храниться в основном каталоге резерва
target_dir = 'F:\\Backup'  # Подставьте тот путь, который вы будете использовать

# 3. Файлы помещаются в zip-архив
# 4. Текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%Y%m%d')
# Текущее время служит именем zip-архива
now = time.strftime('%H%M%S')

# Создаём каталог, если его ещё нет
if not os.path.exists(today):
    os.mkdir(today)# создание каталога
print('Каталог успешно создан', today)

# Имя zip-файла
target = today + os.sep + now + '.zip'

# 5. Используем команду "7z" для помещения файлов в zip-архив
zip_command = '7z a -tzip -mx5 {0} {1}'.format(target, ' '.join(source))

# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('OK')
else:
    print('Error')