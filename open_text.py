def open_text(textfile):

    '''
    Reads every line in a text file, and saves it as a dictionary.
    Args: A text file.
    '''
    flower_dictionary = {}
    with open(textfile,'r') as f:
        for line in f:
            letter = line.split(': ')[0]
            flower = line.split(': ')[1]
            flower_dictionary[letter] = flower
    return flower_dictionary
