# 从多个CSV文件加载表格（Загрузка таблицы из нескольких CSV файлов）
from CSV import load_table_csv

def load_table(file_paths):
    if len(file_paths) == 0:
        raise ValueError("No file paths provided")  # 如果没有提供文件路径，则抛出异常（Если нет путей к файлам, генерировать исключение）

    header = None
    data = []
    
    for file_path in file_paths:
        file_header, file_data = load_table_csv(file_path)
        if header is None:
            header = file_header  # 设置第一个文件的表头为表格的表头（Установка заголовка первого файла в качестве заголовка таблицы）
        elif file_header != header:
            raise ValueError("Mismatched column structure in files")  # 如果列结构不匹配，则抛出异常（Если структура столбцов не совпадает, генерировать исключение）           
        
        data.extend(file_data)  # 合并数据（Объединение данных）
    
    return header, data