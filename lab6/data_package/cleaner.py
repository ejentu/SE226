def remove_duplicates(lst):
    lst = list(set(lst))
    return lst

def strip_whitespaces(string_list):
    return [s.strip() for s in string_list]
