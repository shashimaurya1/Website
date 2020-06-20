#!/usr/bin/env python
import fnmatch

from setuptools import setup, find_namespace_packages
from setuptools.command.build_py import build_py as build_py_orig

excluded = ['website/settings.py']


class build_py(build_py_orig):
    def find_package_modules(self, package, package_dir):
        modules = super().find_package_modules(package, package_dir)
        return [
            (pkg, mod, file)
            for (pkg, mod, file) in modules
            if not any(fnmatch.fnmatchcase(file, pat=pattern) for pattern in excluded)
        ]


setup(name='greenclothaway',
      version='0.1',
      packages=find_namespace_packages(),
      cmdclass={'build_py': build_py},
      include_package_data=True,
      scripts=['manage.py'],
      install_requires=[
          'asgiref==3.2.7',
          'beautifulsoup4==4.9.1',
          'behave==1.2.6',
          'behave-django==1.3.0',
          'bootstrap4==0.1.0',
          'chardet==3.0.4',
          'Django==3.0.6',
          'django-bootstrap4==1.1.1',
          'django-extensions==2.2.9',
          'django-messages==0.6.0',
          'multimetric==1.1.4',
          'parse==1.15.0',
          'parse-type==0.5.2',
          'Pillow==7.1.2',
          'Pygments==2.6.1',
          'pytz==2020.1',
          'six==1.15.0',
          'soupsieve==2.0.1',
          'sqlparse==0.3.1',
      ]
      )
