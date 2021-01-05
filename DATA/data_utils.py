import os


def return_data_folder_absolute_path():
    """
    Return the folder of data
    :return: Absolute path of this file
    """
    return os.path.dirname(os.path.realpath(__file__))


def return_orfs_folder_absolute_path():
    """
    From folder of data, return the subfolder orfs path
    :return: Absolute path of orfs subfolder
    """
    data_path = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(data_path, 'orfs')
    return data_path


def orfs_files_list():
    """
    Return a list of files that start with a determine pattern
    :return: files list.
    """
    dir_name = return_orfs_folder_absolute_path()
    ficheros = []
    pattern = 'tb_data'
    for file in os.listdir(dir_name):
        if pattern in file:
            ficheros.append(file)
    return ficheros
