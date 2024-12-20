# 合并两个表格（Объединение двух таблиц）
from table_operations import Table

def concat(table1, table2):
    if table1.header != table2.header:
        raise ValueError("Tables have different headers")  # 如果两个表格的表头不同，则抛出异常（Если таблицы имеют разные заголовки, генерировать исключение）
    return Table(table1.data + table2.data, table1.header)  # 返回合并后的表格（Возврат объединенной таблицы）

# 按行号分割表格（Разделение таблицы по номеру строки）
def split(table, row_number):
    return Table(table.data[:row_number], table.header), Table(table.data[row_number:], table.header)  # 返回分割后的两个表格（Возврат двух таблиц после разделения）