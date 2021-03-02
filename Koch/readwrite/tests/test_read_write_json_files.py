from Kock.readwrite.read_write_json_files import *
from Kock.readwrite.read_input_files import *
from Data.data_utils import *
import unittest


class TestReadWriteOrfJsonFile(unittest.TestCase):

    def setUp(self):
        print('Cargando ficheros tb_functions')
        dir_data_path = return_data_folder_absolute_path()
        print('Ruta de los datos: {}'.format(dir_data_path))
        file_name = 'tb_functions.pl'
        self.classes, self.functions = (read_functions_file(dir_data_path, file_name))

    def test_classes_count(self):
        dir_data_path = return_data_folder_absolute_path()
        print('tests de clases escritas en json file')
        file_name = 'classes.json'
        if write_json_file(dir_data_path, file_name, self.classes) != 0:
            with self.assertRaises(TypeError):
                print(TypeError)
        new_classes = read_json_file(dir_data_path, file_name)
        self.assertEqual(len(self.classes), len(new_classes))

    def test_functions_count(self):
        dir_data_path = return_data_folder_absolute_path()
        print('tests de funciones escritas en json file')
        file_name = 'functions.json'
        if write_json_file(dir_data_path, file_name, self.functions) != 0:
            with self.assertRaises(TypeError):
                print(TypeError)
        new_functions = read_json_file(dir_data_path, file_name)
        self.assertEqual(len(self.functions), len(new_functions))


if __name__ == '__main__':
    unittest.main()