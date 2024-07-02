def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = []
    number = 0
    words = file_contents.split()
    for word in words:
        number = number + 1
    print(f"This document contains {number} words.")

def dict():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    alpha = file_contents.lower()
    letters_count = {}
    for l in alpha:
        if l.isalpha():
            if l in letters_count:
                letters_count[l] += 1
            else:
                letters_count[l] = 1
    list_of_dicts = [{key: value} for key, value in letters_count.items()]
    
    sorted_list = sorted(list_of_dicts, key=lambda x: list(x.values())[0], reverse=True)
    for d in sorted_list:
        key = next(iter(d))
        value = d[key]
        print(f"The '{key}' character was found {value} times.")



main()
dict()