import sys


def fibonacci():
    a = 0
    b = 1
    yield a
    while True:
        yield b
        a, b = b, a+b


def print_fibonacci(counter):
    index = 1
    if counter < 0:
        counter = sys.maxsize

    for item in fibonacci():
        if index >= counter:
            break
        else:
            print(item)
            index += 1


if __name__ == '__main__':
    print('Enter length of Fibonacci series to display: ', end='', flush=True)
    data = input()
    try:
        print_fibonacci(int(data))
    except ValueError:
        print('ERROR: Only int values allowed.')