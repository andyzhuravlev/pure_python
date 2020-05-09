
class MyManager:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print_level(self, text: str):
        print(' ' * self.level + text)


if __name__ == '__main__':
    with MyManager() as my_man:
        my_man.print_level('Hello')
        with my_man:
            my_man.print_level('World')
            with my_man:
                my_man.print_level('ahead!')
