import unittest
from unittest.mock import patch
from main import find_people, find_shelf, list_docs, add_doc, delete_document, move_document, add_shelf, list_shelves, \
    delete_shelf, do_command, commands


class TestMain(unittest.TestCase):
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

    def test_1_find_people(self):
        print('\n' + 'Проверяем find_people'.center(40, '-'))
        self.assertEqual(find_people(self.documents, self.directories, '2207 876234'), 'Василий Гупкин')

    def test_2_find_shelf(self):
        print('\n' + 'Проверяем find_shelf'.center(40, '-'))
        self.assertEqual(find_shelf(self.documents, self.directories, '11-2'), '1')

    def test_3_list_docs(self):
        print('\n' + 'Проверяем list_docs'.center(40, '-'))
        self.assertIn({'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'}, list_docs(self.documents,
                                                                                                     self.directories))

    def test_4_add_doc(self):
        print('\n' + 'Проверяем add_doc'.center(40, '-'))
        self.assertTrue(add_doc(self.documents, self.directories, doc_number='13', doc_type='license',
                                doc_name='Mr. Voland', shelf_number='13', create_shelf='y'))

    def test_5_delete_document(self):
        print('\n' + 'Проверяем delete_document'.center(40, '-'))
        self.assertEqual(delete_document(self.documents, self.directories, doc_number='11-2'), (True, True))

    def test_6_move_document(self):
        print('\n' + 'Проверяем move_document'.center(40, '-'))
        self.assertTrue(move_document(self.documents, self.directories, doc_number='2207 876234', shelf_number='5',
                                      create_shelf='y'))

    def test_7_add_shelf(self):
        print('\n' + 'Проверяем add_shelf'.center(40, '-'))
        self.assertTrue(add_shelf(self.documents, self.directories, shelf_number='100'))

    def test_8_list_shelves(self):
        print('\n' + 'Проверяем list_shelves'.center(40, '-'))
        self.assertTrue(list_shelves(self.documents, self.directories, ))

    def test_90_delete_shelf(self):
        print('\n' + 'Проверяем delete_shelf'.center(40, '-'))
        self.assertTrue(delete_shelf(self.documents, self.directories, '2', '3'))

    @patch('builtins.input')
    def test_91_delete_shelf(self, m_input):
        print('\n' + 'Проверяем delete_shelf'.center(40, '-'))
        m_input.side_effect = ['3', 'n']
        self.assertTrue(delete_shelf(self.documents, self.directories))

    def test_92_do_command(self):
        print('\n' + 'Проверяем do_command'.center(40, '-'))
        self.assertTrue(do_command(self.documents, self.directories, 'ls', commands))

    @patch('builtins.input')
    def test_93_do_command(self, m_input):
        print('\n' + 'Проверяем do_command'.center(40, '-'))
        m_input.side_effect = ['13']
        self.assertEqual(do_command(self.documents, self.directories, 's', commands), '13')

    @patch('builtins.input')
    def test_94_do_command(self, m_input):
        print('\n' + 'Проверяем do_command'.center(40, '-'))
        m_input.side_effect = ['111', 'test', 'user', '111', 'y']
        self.assertTrue(do_command(self.documents, self.directories, 'a', commands))
        list_shelves(self.documents, self.directories)
        list_docs(self.documents, self.directories)
