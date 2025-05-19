import pandas as pd

class FileHandler:
    def file_open(self):
        try:
            file_name = input(u'Введите имя файла: ')  # Запрашиваем имя файла у пользователя
            if file_name != "var2.csv":
                raise ValueError(u'Неверное имя файла')

            self.df = pd.read_csv(file_name)
            print(u'Файл открыт')

        except (FileNotFoundError, ValueError) as e:
            print(e)  # Выводим соответствующее сообщение об ошибке
        except Exception:
            print(u'Не удалось открыть файл')

        
    def check_empty(self):
        try:
            if self.df.empty:  # Проверяем, пуст ли DataFrame
                raise ValueError  # Вызываем исключение, если файл пуст
            print(u'Файл содержит данные')
        except AttributeError:
            print(u'Файл не был открыт')
        except ValueError:
            print(u'Файл пуст')

    def check_structure(self):
        try:
            if not isinstance(self.df, pd.DataFrame):  # Проверяем, DataFrame ли это
                raise TypeError
            print(u'Структура файла правильная')
        except AttributeError:
            print(u'Файл не был открыт')
        except TypeError:
            print(u'Неправильная структура файла: ожидается таблица, а получен текст')
        except pd.errors.ParserError:
            print(u'Ошибка парсинга: файл не является корректной таблицей')

    def check_header(self, expected_columns):
        try:
            actual_columns = list(self.df.columns)
            if actual_columns != expected_columns:
                raise ValueError
            print(u'Заголовок корректен')
        except AttributeError:
            print(u'Файл не был открыт')
        except ValueError:
            print(u'Ошибка в первом ряду: заголовок не соответствует ожидаемому')

file_handler = FileHandler()
file_handler.file_open()
file_handler.check_structure()
file_handler.check_empty()
file_handler.check_header(["Участники гражданского оборота", "Тип операции", "Сумма операции",
                           "Вид расчета","Место оплаты","Терминал оплаты","Дата оплаты","Время оплаты",
                           "Результат операции", "Cash-back","Сумма cash-back"])  
       


   
       

        