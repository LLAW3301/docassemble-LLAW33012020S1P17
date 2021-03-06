import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LLAW33012020S1P17',
      version='0.0.1',
      description=('CBS Inc. NDIS Advisor'),
      long_description='# P17\r\n\r\nCBS - NDIS Advisor 1\r\n\r\n## Author\r\n\r\nNicole Catabran, cata0036@flinders.edu.au\r\nGale del Pilar, delp0018@flinfers.edu.au\r\nSamara Shute, shut0017@flinders.edu.au\r\nCorina Catsiavas, cats0004@flinders.edu.au\r\n\r\n** FINAL VERSION **\r\n',
      long_description_content_type='text/markdown',
      author='Nicole Catabran, Samara Shute, Corina Catsiavas, Gale del Pilar',
      author_email='cata0036@flinders.edu.au, shut0017@flinders.edu.au, cats0004@flinders.edu.au, delp0018@flinders.edu.au',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LLAW33012020S1P17/', package='docassemble.LLAW33012020S1P17'),
     )

