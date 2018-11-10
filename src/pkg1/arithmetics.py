from sys import stdin


def main(in_file, out_file):
    a = int(in_file.readline())
    b = int(in_file.readline())
    print(a + b, file=out_file)
    print(a - b, file=out_file)
    print(a * b, file=out_file)


if __name__ == '__main__':
    main(stdin, None)
