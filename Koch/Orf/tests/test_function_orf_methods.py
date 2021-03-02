from Kock.Orf.function_orf_methods import *
from Kock.readwrite.read_input_files import *
from Kock.readwrite.read_write_json_files import *
from Data.data_utils import *
import unittest


class TestFunctionOrfMethods(unittest.TestCase):

    def setUp(self):
        # print('Actualizando el fichero json')
        # update_json_tb_functions_files()
        file_name = 'functions.json'
        print('Cargando fichero {}'.format(file_name))
        folder = return_data_folder_absolute_path()
        self.func_dict = read_json_file(folder, file_name)
        self.func_df = df_function_transform(self.func_dict)

    def test_count_class_by_description(self):
        self.assertEqual(count_class_by_description(self.func_df, 'hydro'), 35)

    def test_count_orf_by_class_type(self):
        self.assertTrue(type(count_orf_by_class(self.func_df)) is pd.DataFrame)
        self.assertTrue(type(count_orf_by_class(self.func_df, '[1,1,1,1]')) is int)

    def test_count_orf_by_class_by_value(self):
        self.assertEqual(count_orf_by_class(self.func_df).shape[0], 102)
        self.assertEqual(count_orf_by_class(self.func_df, '[6,0,0,0]'), 606)


if __name__ == '__main__':
    unittest.main()
