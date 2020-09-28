

def repeated_word(mystr):
    try:
        word_list = []
        for word in mystr.split():
            if word.lower() in word_list:
                return word.lower()
            word_list.append(word.lower())
        return None
    except AttributeError as error:
        raise error
