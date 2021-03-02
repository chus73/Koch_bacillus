import matplotlib.pyplot as plt
import numpy as np


def simple_vertical_bar_graph(y, title="", x_title="", y_title="", labels=[""]) :
    """
    Show vertical graph from parameters.
    Args:
        x (:obj:`list`) : String list, with bases name.
        y (:obj:`list`) : Integer list, with total services.
        title (:obj:`string`) : string. Graph title.
    Return:
        None
    """
    fig = plt.figure(figsize=(10, 6), dpi=100)
    g = fig.add_subplot(111)
    x_pos = np.arange(len(labels))
    plt.bar(x_pos, y, align="center")
    g.set_title(title)
    g.set_ylabel(y_title)
    g.set_xlabel(x_title)
    plt.xticks(x_pos, labels)
    plt.show()


def simple_horizontal_bar_graph(y, title="", x_title="", y_title="", labels=[""]):
    """
    Show horizontal bar chart from parameters.
    Args:
        y (:obj:`list`) : Integer list, with total services.
        title (:obj:`string`) : string. Graph title.
    Return:
        None
    """
    fig = plt.figure(figsize=(10, 6), dpi=100)
    if len(y) == 1:
        y.insert(0, 0)
        labels.insert(0,'')
        y.append(0)
        labels.append('')
    y_pos = np.arange(len(labels))
    g = fig.add_subplot(111)
    plt.barh(y_pos, y, align="center")
    g.set_title(title)
    g.set_ylabel(y_title)
    g.set_xlabel(x_title)
    plt.yticks(y_pos, labels)
    plt.show()


if __name__ == '__main__':
    y = [10, 20, 30, 40, 50]
    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    title = 'test_graph'
    x_title = 'x title'
    y_title = 'y title'
    simple_vertical_bar_graph(y, title, x_title, y_title, labels)
    simple_horizontal_bar_graph(y, title, x_title, y_title, labels)
