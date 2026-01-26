def swap_case(s):
    new_s = []
    for i in s:
        if i == i.lower():
            new_s.append((i.upper()))
        else:
            new_s.append((i.lower()))
    return "".join(new_s)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)