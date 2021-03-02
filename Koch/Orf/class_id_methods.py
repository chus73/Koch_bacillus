from Kock.readwrite.read_write_json_files import *
from Kock.Orf.utils import *


def class_id_by_description(my_dict, description):
    """
    From class dict return the class_id by description
    :param my_dict: The class dictionary
    :param description: The description for which looking for
    :return: The class identificator. None otherwise
    """
    for k, v in my_dict.items():
        if v.lower().strip() == description.lower().strip():
            return k


def class_number_by_dimensions(class_dic):
    """
    From class dict retrieve the class id which compound
    of 4 dimensions in array structure. The dimension number
    is compounded by divisors.
    :param class_dic: class dictionary
    :return: dictionary with the number of classes by dimensions
    between 2 and 9. The dimension is decomposed by its dimensions.
    """
    # Construimos el diccionario
    dim_number = {
        'M_2': 0, 'M_3': 0, 'M_4': 0, 'M_5': 0,
        'M_6': 0, 'M_7': 0, 'M_8': 0, 'M_9': 0
    }
    # Recorremos el diccionario de clases
    for k in class_dic.keys():
        # Cada Classes_Id tiene 4 dimensiones
        k = json.loads(k)
        for dim in k:
            if dim > 1:
                # Obtenemos sus divisiones
                div = number_div(dim)
                for d in div:
                    if 2 <= d <= 9:
                        key = 'M_' + str(d)
                        dim_number[key] += 1
    return dim_number


if __name__ == '__main__':
    # Leemos el fichero con las clases
    folder = return_data_folder_absolute_path()
    file_name = 'classes.json'
    class_dict = read_json_file(folder, file_name)
    for k,v in class_dict.items():
        print('{}: {}'.format(k, v))

    description = 'Chelatases '

    print('Class_id by description')
    result = class_id_by_description(class_dict, description)
    print(result)

    print('class number by dimension')
    result = class_number_by_dimensions(class_dict)
    for k, v in result.items():
        print(k, v)
