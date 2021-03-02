from Kock.drawing.bar_graph import *
from Kock.Orf.function_orf_methods import *
from Kock.Orf.class_id_methods import *
from Kock.Orf.orf_relation_methods import *
from Kock.readwrite.read_input_files import *


if __name__ == '__main__':
    # Lectura del fichero tb_functions.
    classes, functions = read_input_files_general()
    df_function = df_function_transform(functions)

    # Pregunta 1.1
    pregunta = '1.1'
    title = 'Número de ORFs por clase (Top 10)'
    result = count_orf_by_class(df_function)
    print('{} - {}.'.format(pregunta, title))
    result = result.nlargest(10, 'ORF')
    print(result)
    y = list(result['ORF'])
    labels = list(result.index)
    simple_horizontal_bar_graph(y, title, labels=labels)

    # Pregunta 1.2
    description = 'Respiration'
    class_id = class_id_by_description(classes, description)
    num_orf = count_orf_by_class(df_function, class_id)
    print('1.2 - Número de ORFs para la clase {}, con identificador {}: {}'.format(description, class_id, num_orf))

    # Pregunta 2.1
    description = 'protein'
    pregunta = '2.1'
    title = 'Número de clases con descripción "' + description + '" y uno o más ORF'
    result = count_class_by_description(df_function, description)
    print('{} - {}: {}'.format(pregunta, title, result))
    pregunta = ['pregunta: ' + pregunta]
    simple_horizontal_bar_graph([result], title, labels=pregunta)

    # Pregunta 2.2
    rel_dic = read_input_files_detallada()
    description = 'hydro'
    pregunta = '2.2'
    long = 13
    title = 'Promedio de ORFs tipo "' + description + '".'
    result = average_orf_by_word(df_function, rel_dic, description, long)
    print('{} - Promedio de ORFs cuya descripción contiene la palabra "{}" y '
          'es de una longitud de {}: {}.'.format(pregunta, description, long, result))
    pregunta = ['pregunta: ' + pregunta]
    simple_horizontal_bar_graph([result], title, labels=pregunta)

    # Pregunta 3
    title = 'Número de clases por dimensión'
    pregunta = '3'
    print('{} - {}'.format(pregunta, title))
    dim_dic = class_number_by_dimensions(classes)
    x = []
    y = []
    for k, v in dim_dic.items():
        print('{}: {} clases.'.format(k, v))
        y.append(k)
        x.append(v)
    x_title = 'Dimensiones'
    y_title = '# Clases'
    simple_vertical_bar_graph(x, title, x_title, y_title, y)
