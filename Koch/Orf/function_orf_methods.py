from Kock.readwrite.read_write_json_files import *
import pandas as pd


def df_function_transform(func_dict):
    """
    From function ORF dict convert to dataframe structure.
    :param func_dict: function ORF dict
    :return: function dataframe
    """
    col_names = ['Class_Id', 'Gen', 'ORF_desc']
    functions_df = pd.DataFrame.from_dict(func_dict, orient='index', columns=col_names)
    functions_df['ORF'] = functions_df.index
    return functions_df


def count_orf_by_class(func_df, class_id=""):
    """
    Return the number of ORF by Class.
    The class is an optional parameter. When it is given,
       return the number of ORF for this class.
    :param func_df: DataFrame with function of bacillus's ORF.
    :param class_id: list of 4 number of dimensions.
    :return: Number of ORF. Integer
    """
    if class_id == '':
        df = func_df.groupby('Class_Id').count()
        df['Class_Id'] = df.index
        df = df[['ORF']]
        return df
    else:
        df = func_df[func_df['Class_Id'] == class_id]
        return len(df.index)


def count_class_by_description(function_df, desc):
    """
    From function ORF dataframe looks for the word param in
    the description ORF field.
    :param function_df: function ORF dataframe
    :param desc: The searched word
    :return: The number of description which contain the searched word.
    """
    df = function_df[function_df['ORF_desc'].str.contains(desc)]
    df = df.groupby('Class_Id').count()
    return len(df.index)


if __name__ == '__main__':
    # Leemos el fichero json de funciones ORF

    file_name = 'functions.json'
    folder = return_data_folder_absolute_path()
    functions = read_json_file(folder, file_name)
    df_function = df_function_transform(functions)

    result = count_orf_by_class(df_function)
    print('1.1 - Número de ORFs por clase:')
    for i, r in result.iterrows():
        print(i, r['ORF'])

    class_id = '[6,0,0,0]'
    result = count_orf_by_class(df_function, class_id)
    print('Número de ORF de la clase {}: {}'.format(class_id, result))

