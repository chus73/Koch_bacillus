from Kock.Orf.function_orf_methods import *
from Kock.readwrite.read_input_files import *
from Kock.readwrite.read_write_json_files import *
from Kock.Orf.orf_relation_methods import *
from Data.data_utils import *
import unittest


class TestOrfRelationMethods(unittest.TestCase):

    def setUp(self):
        dir_name = return_data_folder_absolute_path()
        file_name = 'functions.json'
        func_dict = read_json_file(dir_name, file_name)
        # Pasamos a dataframe
        self.func_df = df_function_transform(func_dict)

        file_name = 'orfs.json'
        print('Cargando fichero {}'.format(file_name))
        dir_name = return_orfs_folder_absolute_path()
        self.orfs_dict = read_json_file(dir_name, file_name)

    def test_average_orf_by_word(self):
        word = 'hydro'
        long = 13
        resp = average_orf_by_word(self.func_df, self.orfs_dict, word, long)
        self.assertEqual(resp, 36.0)


if __name__ == '__main__':
    unittest.main()
