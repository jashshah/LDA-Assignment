import os
from os.path import dirname
from os.path import join
import glob
def load_author_text(author, nameoftext):
    """ Loads a text file according to the author and the name of the text. Parameters
    ----------
    author : Name of the author

    nameoftext: Name of the author's text

    Returns
    ----------
    A string containing the text
    """
    module_path = dirname(__file__)
    with open(join(module_path, 'data', author, nameoftext + '.txt'), 'r', encoding='utf8') as myfile:
        text_file = myfile.read().replace('\n', '')
        return text_file

def load_author(author):
    """Loads all the text files belonging to a particular author
    Parameters
    ----------
    author : Name of the author

    Returns
    ----------
    A list containing five texts of the author
    """
    module_path = dirname(__file__)
    list_text = []
    for infile in glob.glob(os.path.join(module_path, 'data', author, '*.txt')):
        with open(infile, 'r', encoding='utf8') as file:
            list_text.append(file.read().replace('\n', ''))
    return list_text
