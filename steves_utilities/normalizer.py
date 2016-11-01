from re import sub


def normalize_string(string):

    return sub(r'\s+', ' ', sub(r'[^0-9a-zA-Z]', ' ', string).lower()).strip()