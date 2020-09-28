import re 

def repeated_word(mystr):
    """
    Will find the first repeated word in a text.
    """
    try:
        word_list = []
        for word in mystr.split():
            word = re.findall(r'[A-Za-z]+', word.lower())
            if word in word_list:
                return word[0]
            word_list.append(word)
        return None
    except AttributeError as error:
        raise error