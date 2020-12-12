def find_people(documents, directories, doc_number=''):
    """p – people – команда спросит номер документа и выведет имя человека, которому он принадлежит"""
    doc_number = doc_number if doc_number else input('\nВведите номер документа: ')
    message = 'Человек с таким номером документа не найден'
    result = None
    if doc_number:
        for doc in documents:
            if doc['number'] == doc_number:
                message = 'Имя человека с документом "' + doc_number + '": ' + doc['name']
                result = doc['name']
    print(message)
    return result


def find_shelf(documents, directories, doc_number=''):
    """s – shelf – команда спросит номер документа и выведет номер полки, на которой он находится"""
    doc_number = doc_number if doc_number else input('\nВведите номер документа: ')
    message = 'Такого номера документа на полках нет'
    result = None
    if doc_number:
        for number, shelf in directories.items():
            if doc_number in shelf:
                message = 'Документ "' + doc_number + '" находится на полке №' + number
                result = number
    print(message)
    return result


def list_docs(documents, directories):
    """l – list – команда выведет список всех документов"""
    message = ''
    result = []
    if not documents:
        print('Документы не найдены')
        return result
    print('Список документов в каталоге:')
    for doc in documents:
        message += "- " + doc['type'] + ' "' + doc['number'] + '" "' + doc['name'] + '" \n'
        result.append({'type': doc['type'], 'number': doc['number'], 'name': doc['name']})
    print(message[:-2])
    return result


def add_doc(documents, directories, doc_number='', doc_type='', doc_name='', shelf_number='', create_shelf=''):
    """a – add – команда добавит новый документ в каталог и в перечень полок"""
    doc_data = {}
    message = 'Документ не добавлен! Возврат в главное меню...'
    print('Добавляем данные нового документа')
    doc_number = doc_number if doc_number else input('Введите номер документа: ')
    if not doc_number:
        print('Ошибка! Номер документа не может быть пустым!')
        print(message)
        return False
    doc_type = doc_type if doc_type else input('Введите тип документа: ')
    if not doc_type:
        print('Ошибка! Тип документа не может быть пустым!')
        print(message)
        return False
    doc_name = doc_name if doc_name else input('Введите имя владельца документа: ')
    if not doc_name:
        print('Ошибка! Имя владельца документа не может быть пустое!')
        print(message)
        return False
    shelf_number = shelf_number if shelf_number else input('Введите номер полки: ')
    if not (shelf_number in directories):
        choice = create_shelf if create_shelf else input('Полка не существует, создать [y/n]? ')
        if not (choice == 'y') or not (add_shelf(documents, directories, shelf_number)):
            print(message)
            return False
    doc_data['type'] = doc_type
    doc_data['number'] = doc_number
    doc_data['name'] = doc_name
    documents.append(doc_data)
    shelf = directories.get(str(shelf_number), [])
    shelf.append(doc_number)
    print('Документ добавлен')
    return True


def delete_document(documents, directories, doc_number=''):
    """d – delete – команда спросит номер документа и удалит его из каталога и из перечня полок"""
    doc_number = doc_number if doc_number else input('\nВведите номер документа: ')
    messages = ['Такого документа нет в каталоге', 'Такого документа на полках нет']
    result_catalogue_delete = False
    result_shelf_delete = False
    if doc_number:
        for doc in documents:
            if doc['number'] == doc_number:
                documents.remove(doc)
                messages[0] = 'Документ "' + doc_number + '" удалён из каталога'
                result_catalogue_delete = True
        for number, shelf in directories.items():
            if doc_number in shelf:
                shelf.remove(doc_number)
                messages[1] = 'Документ "' + doc_number + '" удален с полки №' + number
                result_shelf_delete = True
    print(*messages, sep='\n')
    return result_catalogue_delete, result_shelf_delete


def move_document(documents, directories, doc_number='', shelf_number='', create_shelf=''):
    """m – move – команда спросит номер документа и целевую полку и переместит его с текущей полки на целевую """
    doc_number = doc_number if doc_number else input('\nВведите номер документа: ')
    shelf_number = shelf_number if shelf_number else input('Введите целевую полку: ')
    messages = ['Такого документа нет в каталоге', 'Такого документа на полках нет', 'Номер полки не введен',
                'Невозможно переместить документ']
    if not shelf_number:
        print(messages[2])
        return False
    if not (shelf_number in directories):
        choice = create_shelf if create_shelf else input('Полки не существует, создать [y/n]? ')
        if not (choice == 'y') or not (add_shelf(documents, directories, shelf_number)):
            print(messages[3])
            return False
    messages[2] = ''  # if shelf exist then simply delete corresponding error message
    if doc_number:
        for doc in documents:
            if doc['number'] == doc_number:
                messages[0] = ''  # if document exist in catalogue then simply delete corresponding error message
        for number, shelf in directories.items():
            if doc_number in shelf:
                shelf.remove(doc_number)
                directories.get(shelf_number, []).append(doc_number)
                print('Документ ' + doc_number + ' перемещен на полку №' + shelf_number)
                return True
    print(*messages, sep='\n')
    return False


def add_shelf(documents, directories, shelf_number=''):
    """as – add shelf – команда спросит номер новой полки и добавит ее в перечень"""
    message = 'Полка не добавлена! Возврат в главное меню...'
    shelf_number = shelf_number if shelf_number else input('Введите номер полки: ')
    try:
        shelf_number = int(shelf_number)
    except ValueError:
        print('Ошибка! Введено не числовое значение!')
        print(message)
        return False
    if 0 > shelf_number:
        print('Ошибка! Неверный номер полки!')
        print(message)
        return False
    if str(shelf_number) in directories:
        print('Ошибка! Полка с таким номером уже существует!')
        print(message)
        return False
    directories[str(shelf_number)] = []
    print('Полка добавлена')
    return True


def list_shelves(documents, directories):
    """ls – list shelves – команда выведет список полок с документами"""
    if not directories:
        print('Полки не найдены')
        return False
    print('Список полок с документами:')
    for count, shelf in directories.items():
        print(count + '. ' + str(shelf))
    return True


def delete_shelf(documents, directories, shelf_number='', receiving_shelf=''):
    """ds – delete shelf – команда спросит номер полки и удалит её и все документы на ней"""
    shelf_number = shelf_number if shelf_number else input('\nВведите номер полки: ')
    message = 'Такой полки не существует'
    result = False
    if shelf_number and shelf_number in directories:
        # Make copy to prevent breaking loop iteration while item delete with delete_document()
        docs = directories.get(shelf_number).copy()
        if not (docs is None):
            if len(docs) > 0:
                choice = receiving_shelf if receiving_shelf else input('На полках присутствуют документы, если хотите '
                                                                       'переместить их, введите номер полки, иначе '
                                                                       'нажмите "n": ')
                if choice == 'n':
                    for doc in docs:
                        delete_document(documents, directories, doc)
                else:
                    for doc in docs:
                        if not move_document(documents, directories, doc, choice):
                            print('Ошибка перемещения документов. Удаление полки отменено!')
                            return result
            directories.pop(shelf_number)
            message = 'Полка удалена'
            result = True
    print(message)
    return result


def show_help():
    print()
    print(find_people.__doc__)
    print(find_shelf.__doc__)
    print(list_docs.__doc__)
    print(add_doc.__doc__)
    print(delete_document.__doc__)
    print(move_document.__doc__)
    print(add_shelf.__doc__)
    print(list_shelves.__doc__)
    print(delete_shelf.__doc__)


commands = {
    'p': find_people,
    'people': find_people,
    's': find_shelf,
    'shelf': find_shelf,
    'l': list_docs,
    'list': list_docs,
    'a': add_doc,
    'add': add_doc,
    'd': delete_document,
    'delete': delete_document,
    'm': move_document,
    'move': move_document,
    'as': add_shelf,
    'add shelf': add_shelf,
    'ls': list_shelves,
    'list shelves': list_shelves,
    'ds': delete_shelf,
    'delete shelf': delete_shelf,
    'h': show_help,
    'help': show_help
}


def do_command(documents, directories, command: str, commands: dict):
    func = commands.get(command, None)
    if func:
        return func(documents=documents, directories=directories)
    else:
        print('Введена неверная команда. Введите "q" для выхода и нажмите Enter...')
        return False


def process_commands(documents, directories):
    print('Добро пожаловать в справочник!')
    while True:
        command = input('\nВведите команду или введите "help" и нажмите Enter: ')
        if command == 'q' or command == 'quit':
            print('Всего хорошего!')
            break
        else:
            do_command(documents, directories, command, commands)


if __name__ == '__main__':
    documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ]
    directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
    }

    process_commands(documents, directories)
