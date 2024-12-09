def append_to_file(filename, text):
    with open(filename, 'a', encoding='utf-8' if 'utf-8' in filename else 'cp1251') as f:
        f.write(text)
append_to_file('utf-8.txt', ' мир')
append_to_file('windows-1251.txt', ' мир')