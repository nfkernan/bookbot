def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = []
    number = 0
    words = file_contents.split()
    for word in words:
        number = number + 1
    print(f"This book contains {number} words.")

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
    print(letters_count)

main()
dict()