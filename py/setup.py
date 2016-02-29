"""
Copyright 2016 Gu Zhengxiong <rectigu@gmail.com>

This file is part of Pat.

Pat is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Pat is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Pat.  If not, see <http://www.gnu.org/licenses/>.
"""


from setuptools import setup

from pat import (
    PROGRAM_NAME, PACKAGE_NAME, __version__, __author__
)


setup(
    name=PROGRAM_NAME,
    version=__version__,
    packages=[PACKAGE_NAME],
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'pat={}.main:main'.format(PACKAGE_NAME)
        ]
    },

    author=__author__,
    author_email='rectigu@gmail.com',
    description='Pat',
    license='GPL-3',
    keywords='Exploit Pattern, Cartesian Product, Mixed Radix',
    url='https://github.com/NoviceLive/{}'.format(PACKAGE_NAME),

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: '
        'GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ]
)
