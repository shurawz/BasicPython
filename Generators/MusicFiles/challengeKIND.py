import os
import fnmatch


def generate(start, extension):
    for path, start, files in os.walk(start):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            absolute_path = os.path.abspath(path)  # create absolute path i.e from the drive
            yield os.path.join(absolute_path, file)  # returning/ yielding it


for g in generate("music", "emp3"):
    print(g)