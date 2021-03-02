from Kock.readwrite.read_input_files import *
from Data.data_utils import *
import unittest


class TestReadTbFunctionsFile(unittest.TestCase):

    def setUp(self):
        print('Cargando fichero tb_functions')
        dir_data_path = return_data_folder_absolute_path()
        print('Ruta de los datos: {}'.format(dir_data_path))
        file_name = 'tb_functions.pl'
        self.classes, self.functions = (read_functions_file(dir_data_path, file_name))

    def test_classes_count(self):
        print('Número de clases leídas')
        self.assertEqual(len(self.classes), 123)

    def test_fuctions_count(self):
        print('Número de funciones leídas')
        self.assertEqual(len(self.functions), 3924)


class TestReadOrfFiles(unittest.TestCase):

    def setUp(self):
        print('Cargando ficheros orfs')
        dir_data_path = return_orfs_folder_absolute_path()
        files_list= orfs_files_list()
        print('Ruta de los datos: {}'.format(dir_data_path))
        self.orfs = read_tb_data_multiprocess(dir_data_path, files_list)

    def test_orf_count(self):
        print('Número total de relaciones leídas')
        self.assertEqual(len(self.orfs), 3924)


if __name__ == '__main__':
    unittest.main()