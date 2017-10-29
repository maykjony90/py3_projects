# library for running external commands
from subprocess import run


def main():
    # you can use either of the below commands
    run(['ls', '-al'])
    run('ls -l'.split(" "))


if __name__ == "__main__":
    main()
