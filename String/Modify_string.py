#to modify the string, wecan convert string into character and then modify it by adding the modified character into a new string.
def modified_string(string, position, character):
    l = list(string)
    l[int(position)] = character

    return "".join(l)


if __name__ == "__main__":
    string =input()
    position, character = input().split()
    result = modified_string(string, position, character)
    print(result)