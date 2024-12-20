# 将表格保存为多个CSV文件（Сохранение таблицы в несколько CSV файлов）
from CSV import save_table_csv

def save_table(header, data, file_path, max_rows):
    if max_rows <= 0:
        raise ValueError("max_rows must be greater than 0")  # 如果最大行数不大于0，则抛出异常（Если максимальное количество строк <= 0, генерировать исключение）
    
    start = 0
    while start < len(data):
        end = min(start + max_rows, len(data))  # 计算结束索引（Вычисление индекса окончания）
        save_table_csv(header, data[start:end], f"{file_path}_{start//max_rows+1}.csv")  # 保存当前数据块（Сохранение текущего блока данных）
        start = end
    