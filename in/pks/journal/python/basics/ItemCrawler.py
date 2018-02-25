from pprint import pprint as pp


def crawl(iterable):
    if not hasattr(iterable, '__iter__'):
        return

    _iter = iter(iterable)

    flag = True
    while flag:
        try:
            print('crawled: ' + str(next(_iter)))
        except StopIteration as siex:
            print('Ends')
            flag = False
        except TypeError:
            print('Invalid type provided. It mus be iterable.')
            flag = False


def gen234():
    print('this is a generator function')
    print('about to yield 2')
    yield [2, 3, 4]
    print('about to yield 3')
    yield ['apple', 'banana', 'mango']
    print('about to yield 4')
    yield ('RED', 'BLUE', 'GREEN', 'WHITE', 'BLACK')
    # yield 'exit'


if __name__ == '__main__':
    g = gen234()
    while True:
        try:
            data = next(g)
        except StopIteration:
            data = input()

        pp(data)

        if data == 'exit':
            break;
        else:
            # colors = ['red', 'blue', 'green', 'grey', 'cyan', 'violet', 'white', 'black', 'indigo', 'auburn']
            crawl(data)

