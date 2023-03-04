def read_file(filename=None, start=None, end=None):
    filename = 'file1.txt' if filename is None else filename
    global encoding
    encoding = 'utf8'
    try:
        test_file = open(filename, 'r', encoding=encoding)
        test_file.readlines()
        test_file.close()
    except UnicodeDecodeError:
        encoding = 'utf16'
    with open(filename, 'r', encoding=encoding) as f:
        contents = f.readlines()
    if start or end:
        return '\n'.join(map(lambda x: x.rstrip(), contents[start:end]))
    return '\n'.join(map(lambda x: x.rstrip(), contents))
