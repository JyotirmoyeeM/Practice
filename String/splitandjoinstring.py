def split_and_join(s):
    words = s.split(" ")
    return "-".join(words)

if __name__ == '_main__':
    s = input()
    result = split_and_join(s)
    print(result)
