import csv

# 加载CSV文件（Загрузка CSV файла）
def load_table_csv(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # 读取表头（Чтение заголовка）
        data = [row for row in reader]  # 读取数据行（Чтение строк данных）
    return header, data

# 保存CSV文件（Сохранение CSV файла）
def save_table_csv(header, data, file_path):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)  # 写入表头（Запись заголовка）
        writer.writerows(data)  # 写入数据行（Запись строк данных）