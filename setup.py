1# -*- coding: utf-8 -*-

from os.path import join
from setuptools import setup, find_packages

name = 'uvc.design.canvas'
version = '0.1'
readme = open('README.txt').read()
history = open(join('docs', 'HISTORY.txt')).read()


install_requires = [
    'setuptools',
    'cromlech.browser',
    'dolmen.menu',
    'dolmen.template',
    'grokcore.component',
    'uvclight',
    'zope.interface',
    'zope.security',
    ]


tests_require = [
    ]


setup(name=name,
      version=version,
      description=("UVC Design base package"),
      long_description=readme + '\n\n' + history,
      keywords='',
      author='Novareto',
      author_email='',
      url='',
      license='BSD',
      package_dir={'': 'src'},
      packages=find_packages('src', exclude=['ez_setup']),
      namespace_packages=['uvc', 'uvc.design'],
      include_package_data=True,
      zip_safe=False,
      tests_require=tests_require,
      install_requires=install_requires,
      extras_require={'test': tests_require},
      classifiers=[
          'Environment :: Web Environment',
          'Intended Audience :: Other Audience',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
