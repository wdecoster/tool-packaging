from os import path
import pypandoc

here = path.abspath(path.dirname(__file__))
long_description=pypandoc.convert(path.join(here, 'testing-pandoc-md2rst.md'), 'rst'),

with open("test.rst", 'w') as out:
    out.write(long_description[0])
