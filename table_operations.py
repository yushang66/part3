def new_func():
    # 表格类（Класс таблицы）
        class Table:
            def __init__(self, data, header=None):
                self.header = header  # 表格头部（Заголовок таблицы）
                self.data = data  # 表格数据（Данные таблицы）

    # 根据行号获取行（Получение строк по номеру）
            def get_rows_by_number(self, start, stop=None, copy_table=False):
                if stop is None:
                    stop = len(self.data)
                if copy_table:
                    return Table(self.data[start:stop], self.header)  # 返回表格的副本（Возврат копии таблицы）
                else:
                    return Table(self.data[start:stop], self.header)  # 返回表格视图（Возврат представления таблицы）

    # 根据第一列的值获取行（Получение строк по значению в первом столбце）
            def get_rows_by_index(self, *val, copy_table=False):
                filtered_data = [row for row in self.data if row[0] in val]
                if copy_table:
                    return Table(filtered_data, self.header)  # 返回表格的副本（Возврат копии таблицы）
                else:
                    return Table(filtered_data, self.header)  # 返回表格视图（Возврат представления таблицы）

    # 获取列的数据类型（Получение типа данных столбца）
            def get_column_types(self, by_number=True):
                column_types = {}
                for i, col in enumerate(self.data[0]):
                    if by_number:
                        column_types[i] = type(col).__name__  # 使用列索引（Использование индекса столбца）
                    else:
                        column_types[self.header[i]] = type(col).__name__  # 使用列名（Использование имени столбца）
                return column_types

    # 设置列的数据类型（Установка типа данных столбца）
            def set_column_types(self, types_dict, by_number=True):
                for key, value in types_dict.items():
                    if by_number:
                        self.data = [[value(x) if x != '' else None for x in [row[key] for row in self.data]]
                            for key in self.data[0]]
                    else:
                        self.data = [[value(x) if x != '' else None for x in [row[self.header.index(key)] for row in self.data]]
    # 获取列的值（Получение значений столбца）
    def get_values(self, column=0):
        return [row[column] for row in self.data]

    # 获取单个单元格的值（Получение значения ячейки）
    def get_value(self, column=0):
        return self.data[0][column]

    # 设置列的值（Установка значений столбца）
    def set_values(self, values, column=0):
        for i, value in enumerate(values):
            self.data[i][column] = value

    # 设置单个单元格的值（Установка значения ячейки）
    def set_value(self, value, column=0):
        self.data[0][column] = value

    # 打印表格（Печать таблицы）
    def print_table(self):
        for row in self.data:
                print(row)

    return new_func()

return new_func()