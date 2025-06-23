from core.super_iters import print_hello


NAMES=('Alexandra', 'Nikita', 'Julya', 'Kristina', 'Ritis')


def main():
    print_hello(names=NAMES, exclude_names=['Ritis'], is_random=True)


if __name__ == '__main__':
    main()
