from Kock.readwrite.read_input_files import *
import json


def write_json_file(folder, file_name, my_dicc):
    """
    Write to json file from dictionary.
    :param folder: Folder to save the destination file.
    :param file_name: Name of destination file
    :param my_dicc: Input dictionary.
    :return: 0 if it is right, 1 otherwise.
    """
    try:
        with open(os.path.join(folder, file_name), 'w') as f:
            f.write(json.dumps(my_dicc))
        return 0
    except:
        return 1


def read_json_file(folder, file_name):
    """
    Read a json file from folder
    :param folder: json file's Folder.
    :param file_name: Name of json file to be read.
    :return: A dictionary with the information json file.
    """

    with open(os.path.join(folder, file_name), 'r') as f:
        data = json.load(f)
    return data


def update_json_tb_functions_files():
    """
    Update the classes.json and functions.json with
    the input files.
    :return: None
    """
    print('Cargando fichero tb_functions')
    dir_data_path = return_data_folder_absolute_path()
    file_name = 'tb_functions.pl'
    classes, functions = (read_functions_file(dir_data_path, file_name))

    file_name = 'classes.json'
    if write_json_file(dir_data_path, file_name, classes) == 0:
        print('Fichero {} guardado.'.format(file_name))
    else:
        print('El fichero {} no se ha podido guardar.'.format(file_name))

    file_name = 'functions.json'
    if write_json_file(dir_data_path, file_name, functions) == 0:
        print('Fichero {} guardado.'.format(file_name))
    else:
        print('El fichero {} no se ha podido guardar.'.format(file_name))


def update_json_orfs_file():
    """
    Update the orfs.json file from the tb_data_XX.txt files
    :return: None
    """
    print('Actualizando fichero de relaciones orf')
    orfs = read_input_files_detallada()

    # Escritura json file
    dir_name = return_orfs_folder_absolute_path()
    file_name = 'orfs.json'
    if write_json_file(dir_name, file_name, orfs) == 0:
        print('Fichero {} guardado.'.format(file_name))
    else:
        print('El fichero {} no se ha podido guardar.'.format(file_name))


if __name__ == '__main__':
    update_json_tb_functions_files()
    update_json_orfs_file()
