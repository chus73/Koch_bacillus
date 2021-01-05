import unittest
from Kock.readwrite.tests.test_read_input_files import *
from Kock.readwrite.tests.test_read_write_json_files import *
from Kock.Orf.tests.test_class_id_methods import *
from Kock.Orf.tests.test_function_orf_methods import *
from Kock.Orf.tests.test_orf_relation_methods import *


def suite_test_read_input_files():
    suite = unittest.TestSuite()
    suite.addTest(TestReadTbFunctionsFile('test_classes_count'))
    suite.addTest(TestReadTbFunctionsFile('test_fuctions_count'))
    suite.addTest(TestReadOrfFiles('test_orf_count'))
    return suite


def suite_test_read_write_json_files():
    suite = unittest.TestSuite()
    suite.addTest(TestReadWriteOrfJsonFile('test_classes_count'))
    suite.addTest(TestReadWriteOrfJsonFile('test_functions_count'))
    return suite


def suite_test_class_id_methods():
    suite = unittest.TestSuite()
    suite.addTest(TestClassIdMethods('test_classes_count'))
    suite.addTest(TestClassIdMethods('test_class_id_by_description'))
    suite.addTest(TestClassIdMethods('test_class_number_by_dimensions'))
    return suite


def suite_test_function_orf_methods():
    suite = unittest.TestSuite()
    suite.addTest(TestFunctionOrfMethods('test_count_class_by_description'))
    suite.addTest(TestFunctionOrfMethods('test_count_orf_by_class_type'))
    suite.addTest(TestFunctionOrfMethods('test_count_orf_by_class_by_value'))
    return suite


def suite_test_orf_relation_methods():
    suite = unittest.TestSuite()
    suite.addTest(TestOrfRelationMethods('test_average_orf_by_word'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(failfast=True)
    runner.run(suite_test_read_input_files())
    runner.run(suite_test_read_write_json_files())
    runner.run(suite_test_class_id_methods())
    runner.run(suite_test_function_orf_methods())
    runner.run(suite_test_orf_relation_methods())
