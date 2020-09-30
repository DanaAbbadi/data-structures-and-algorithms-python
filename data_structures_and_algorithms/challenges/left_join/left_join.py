def left_join(dict_1, dict_2):
    """
     LEFT JOINs two hashmaps into a single data structure.
     Arguments:
        dict_1: {dictionary} has word strings as keys, and a synonym of the key as values.
        dict_2: {dictionary} that has word strings as keys, and antonyms of the key as values.
    """
    try:
        output = []
        for key in dict_1:
            if key in dict_2:
                d2 = dict_2[key]
            else:
                d2 = 'Null'

            output.append([key, dict_1[key], d2])
            
        return output
    except Exception:
        print('An error occurred during executing')