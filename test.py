def hello(name):
    if name:
        return f'hello {name}'
    return 'hello world'

if __name__ == '__main__':
    print(hello(None))
    print(hello('luke'))
