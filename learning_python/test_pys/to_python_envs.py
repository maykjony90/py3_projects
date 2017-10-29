from sys import argv
import os
from subprocess import call


def main(argv):
    print(len(argv))
    if len(argv) != 3:
        print("\n\tUSAGE: python to_python_envs <directory> <environment>\n")
        exit(1)

    os.chdir("/home/jony/Documents/python_projects/py3projects/learning_python/{}".format(argv[1]))
    call("source activate {}".format(argv[2]), shell=True)
    print("Environmen: {}\n".format(argv[2]) +
          "Working Directory: {}".format(argv[1]))


if __name__ == "__main__":
    main(argv)
