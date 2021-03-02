from Kock.Orf.class_id_methods import *
from Kock.readwrite.read_input_files import *
from Kock.readwrite.read_write_json_files import *
from Data.data_utils import *
import unittest


class TestClassIdMethods(unittest.TestCase):

    def setUp(self):
        # print('Actualizando el fichero json')
        # update_json_tb_functions_files()
        file_name = 'classes.json'
        print('Cargando fichero {}'.format(file_name))
        folder = return_data_folder_absolute_path()
        self.classes = read_json_file(folder, file_name)

    def test_classes_count(self):
        print('Número de clases leídas')
        self.assertEqual(len(self.classes), 123)

    def test_class_id_by_description(self):
        correct_word = 'Chelatases'
        self.assertEqual(class_id_by_description(self.classes, correct_word), '[4,11,0,0]')

    def test_class_number_by_dimensions(self):
        result = class_number_by_dimensions(self.classes)
        # Comprueba el número de dimensiones devueltas
        self.assertEqual(len(result.keys()), 8)
        # Comprueba el valor por key
        self.assertEqual(result['M_2'], 143)
        self.assertEqual(result['M_4'], 51)
        self.assertEqual(result['M_9'], 3)


if __name__ == '__main__':
    unittest.main()
