def patternSearch(pattern, string):
    strlen = len(string)
    for i in range(0, strlen):
        if string[i:i + len(pattern)] == pattern:
            return i
    return -1


def main():
    pattern = input("enter a pattern: ")
    string = input("enter a string: ")
    print(patternSearch(pattern, string))


main()