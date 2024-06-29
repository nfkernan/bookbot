def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = []
    number = 0
    words = file_contents.split()
    for word in words:
        number = number + 1
    print(number)

main()