import pickle_1
# 从Pickle文件加载表格数据（Загрузка данных таблицы из файла Pickle）
def load_table_pickle(file_path):
    with open(file_path, 'rb') as file:
        data = pickle_1.load(file)  # 反序列化数据（Десериализация данных）
    return data

# 将表格数据保存到Pickle文件（Сохранение данных таблицы в файл Pickle）
def save_table_pickle(data, file_path):
    with open(file_path, 'wb') as file:
        pickle_1.dump(data, file)  # 序列化数据（Сериализация данных）