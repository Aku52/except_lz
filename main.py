from obrabotka import FileHandler  # Импортируем класс из другого файла

# Создаем объект FileHandler
file_handler = FileHandler()

# Запускаем открытие файла
file_handler.file_open()

# Проверяем, был ли файл успешно открыт
if hasattr(file_handler, 'df'):
    file_handler.check_structure()
    file_handler.check_empty()
    file_handler.check_header([
        "Участники гражданского оборота", "Тип операции", "Сумма операции",
        "Вид расчета", "Место оплаты", "Терминал оплаты", "Дата оплаты",
        "Время оплаты", "Результат операции", "Cash-back", "Сумма cash-back"
    ])
