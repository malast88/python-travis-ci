from sys import stdin

def main(input, output):
    a = int(input.readline())
    b = int(input.readline())
    print(a+b, file=output)
    print(a-b, file=output)
    print(a*b, file=output)

if __name__ == '__main__':
    main(stdin, None)