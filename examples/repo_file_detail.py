import os
from gitpandas import ProjectDirectory

__author__ = 'willmcginnis'

if __name__ == '__main__':
    g = ProjectDirectory(working_dir=os.path.abspath('../'))

    b = g.file_detail(include_globs=['*.py'], ignore_globs=['lib/*', 'docs/*'])
    print(b.head(25))

