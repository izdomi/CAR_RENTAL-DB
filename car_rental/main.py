import sys


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    print('Executing movies module ...')


if __name__ == '__main__':
    sys.exit(main())
