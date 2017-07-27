import pypandoc
import sys

long_description=pypandoc.convert(sys.argv[1], 'rst'),

with open("test.rst", 'w') as out:
    out.write(long_description[0])
