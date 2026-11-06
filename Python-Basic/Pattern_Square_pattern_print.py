"""Print square patterns made from stars and row or column numbers."""

N = 5


def pattern_star_square():
    for _ in range(N):
        print("*" * N)


def pattern_row_number():
    for _ in range(N):
        print("".join(str(column) for column in range(1, N + 1)))


def pattern_column_number():
    for row in range(1, N + 1):
        print(str(row) * N)


if __name__ == "__main__":
    pattern_star_square()
    pattern_row_number()
    pattern_column_number()
