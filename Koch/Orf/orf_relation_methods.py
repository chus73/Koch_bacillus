from Data.data_utils import *
from Kock.readwrite.read_write_json_files import *
from Kock.Orf.function_orf_methods import *


def count_orfs_by_orf(rel_dic, orf):
    """
    Return the number of value from dictionary key
    :param rel_dic: dictionary input
    :param orf: dictionary's key
    :return: Number of list elements of dictionary's key
    """
    return len(rel_dic[orf])


def average_orf_by_word(function_df, relation_dic, word, long):
    """
    Search the average number of related ORF with contain
    a specific word and a specific long.
    :param function_df: ORF's Dataframe.
    :param relation_dic: Dictionary with ORF relations.
    :param word: The word searched.
    :param long: The specific long to be searched.
    :return: average float number. The ORF's related with it
    """
    df = function_df[function_df['ORF_desc'].str.contains(word)]
    index_list = []
    n_orf_rel = 0.0
    total_orf = 0.0
    for i, row in df.iterrows():
        desc_list = row['ORF_desc'].split(' ')
        for d in desc_list:
            if d.find(word):
                # Comprobamos si la palabra tiene la longitud debida
                if len(d) == long:
                    index_list.append(i)
                    # Buscamos con cuantos ORFs está relacionado
                    n_orf_rel += count_orfs_by_orf(relation_dic, row['ORF'])
                    total_orf += 1

    return n_orf_rel // total_orf


if __name__ == '__main__':
    # Leemos el fichero functions.json
    dir_name = return_data_folder_absolute_path()
    file_name = 'functions.json'
    func_dict = read_json_file(dir_name, file_name)

    # Pasamos a dataframe
    func_df = df_function_transform(func_dict)
    print(func_df.head())

    # Leemos el fichero orfs.json
    dir_name = return_orfs_folder_absolute_path()
    file_name = 'orfs.json'
    orfs_dict = read_json_file(dir_name, file_name)

    # Calculamos la media de relaciones por orf
    word = 'hydro'
    long = 13
    resp = average_orf_by_word(func_df, orfs_dict, word, long)
    print('Promedio de relaciones de ORF que contienen la palabra dada {}'.format(resp))



