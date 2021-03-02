from Data.data_utils import *
from Kock.readwrite.read_write_json_files import *
from multiprocessing import Queue, Process
import os
import re


def lookup_regex(expr, regex):
    """
    Return True or False if the regex expression has match.
    :param expr: The string where will be searched.
    :param regex: Expression like '^function' or '^class'
    :return: Boolean type.
    """
    result = re.search(regex, expr)
    if result:
        return True
    else:
        return False


def read_functions_file(folder, file_name):
    """
    Read the tb_functions.pl file and split the classes and functions ORF.
    :param file_name: The file name.
    :param folder: Folder which contain the file.
    :return: Two dictionaries, classes and functions from file.
    """
    classes = {}
    functions = {}
    data = []
    with open(os.path.join(folder, file_name)) as f:
        for line in f:
            if lookup_regex(line, '^class'):
                line = re.search("\((.*)\)", line).group(1)
                data.append(re.search("^\[.*\]", line).group(0))
                data.append(re.search('".*', line).group(0))
                # data[0]: Class Id
                # data[1]: Class description
                classes[data[0]] = data[1].replace('"', '')
                data = []
            if lookup_regex(line, '^function'):
                line = re.search("\((.*)\)", line).group(1)
                regex = '(^\w*),(\[.*]),(''.*''),(".*")'
                result = re.search(regex, line)
                for i in range(len(result.groups())):
                    if i == 0:
                        key = result.groups()[0]
                    else:
                        data.append(result.groups()[i])
                functions[key] = data
                for v in functions.values():
                    for d in v:
                        d.replace("'", "")
                data = []
    return classes, functions


def read_tb_data_file(i, data, results_q):
    """
    Read the data from tb_data_XX.txt file and create de dictionary output.
    :param i: Number of process
    :param data: Data from file
    :param results_q: Output Queue with the dictionary
    :return None
    """
    import multiprocessing
    # print('Starting:' , multiprocessing.current_process().name)
    orf_dic = {}
    orf = ''
    orf_rel = []
    for line in data:
        # Waiting for begin(ORF)
        if line.find('begin(') != (-1):
            orf = re.search("\(.*\((.*)\)\)", line).group(1)
        if line.find('tb_to_tb_') != (-1):
            orf_rel.append(re.search("^.*\((\w*)", line).group(1))
        if line.find('end(model(') != (-1):
            orf_dic[orf] = orf_rel
            orf = ''
            orf_rel = []
    print('Finish process {}'.format(i))
    print('Lenght {}'.format(len(orf_dic)))
    results_q.put(orf_dic)


def read_tb_data_multiprocess(folder, fichero_list):
    """
    Main multiprocess for reading tb_data_XX.txt and process it.
    :param folder: Folder's file.
    :param fichero_list: A list with files to be processed.
    :return: dictionary with the files information.
    """

    # Creamos la cola de resultados
    results_q = Queue()
    processes = []

    for i, file in enumerate(fichero_list):
        with open(os.path.join(folder, file)) as f:
            # Lectura del fichero
            data = f.readlines()

        p = Process(target=read_tb_data_file, args=(i, data, results_q))
        processes.append(p)
        print("Starting process {}".format(i))
        p.start()

    print('Waiting to join processes')

    for i, process in enumerate(processes):
        # Espera hasta fin de tareas, máx: 5 segundos
        process.join(5)
        print("Process {} has joined".format(i))

    # Operamos con el resultado
    orf_rel = {}
    while not results_q.empty():
        orf_rel.update(results_q.get())

    return orf_rel


def read_input_files_general():
    """
    Function for automatic reading tb_functions.pl
    :return: Two dictionaries, classes and functions, from information file.
    """
    dir_name = return_data_folder_absolute_path()
    print('Leemos el ficheros de información general del bacilo de Koch.')
    file_name = 'tb_functions.pl'
    classes, functions = (read_functions_file(dir_name, file_name))

    return classes, functions


def read_input_files_detallada():
    """
    Function for automatic reading tb_data_XX.txt files.
    :return: Dictionary with information files structure.
    """
    print('Leemos los ficheros con información detallada sobre el bacilo de Koch.')

    dir_name = return_orfs_folder_absolute_path()
    ficheros = []
    pattern = 'tb_data'
    for file in os.listdir(dir_name):
        if pattern in file:
            ficheros.append(file)
    orfs = read_tb_data_multiprocess(dir_name, ficheros)

    return orfs


if __name__ == '__main__':
        print('Reading files')

        dir_name = "../../Data\\"
        print('Leemos el fichero de los genes y sus clases funcionales.')
        file_name = 'tb_functions.pl'
        classes, functions = (read_functions_file(dir_name, file_name))

        print('Writing files')
        print('Escribimos los datos de los genes y sus clases para su posterior explotación')

        file_name = 'classes.json'
        if write_json_file(dir_name, file_name, classes) == 0:
            print('Fichero {} guardado.'. format(file_name))
        else:
            print('El fichero {} no se ha podido guardar.'.format(file_name))

        file_name = 'functions.json'
        if write_json_file(dir_name, file_name, functions) == 0:
            print('Fichero {} guardado.'.format(file_name))
        else:
            print('El fichero {} no se ha podido guardar.'.format(file_name))

        print('Reading diccionaries')

        file_name = 'classes.json'
        classes = read_json_file(dir_name, file_name)

        file_name = 'functions.json'
        functions = read_json_file(dir_name, file_name)

        # Lectura de los ficheros orfs tipo tb_data_xx.txt
        orfs = read_input_files_detallada()
        print('Longitud total del diccionario: {}'.format(len(orfs)))

        # Escritura json file
        file_name = 'orfs.json'
        if write_json_file(dir_name, file_name, orfs) == 0:
            print('Fichero {} guardado.'.format(file_name))
        else:
            print('El fichero {} no se ha podido guardar.'.format(file_name))
