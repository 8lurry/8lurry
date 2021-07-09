# -*- coding: UTF-8 -*-
# Copyright 2016-2021 Rumma & Ko Ltd
# Copyright 2021 8lurry <sharifmehedi24@outlook.com>
# License: GNU Affero General Public License v3 (see file COPYING for details)

SETUP_INFO = dict(
    name='whitewall',
    version='0.1.0',
    install_requires=['lino-xl'],
    description=('8lurry on the wire'),
    author='8lurry',
    author_email='sharifmehedi24@outlook.com',
    url="https://github.com/8lurry/8lurry",
    license_files=['COPYING'],
    test_suite='tests')

SETUP_INFO.update(classifiers="""
Programming Language :: Python
Programming Language :: Python :: 3
Development Status :: 4 - Beta
Environment :: Web Environment
Framework :: Django
Intended Audience :: HTML readers
License :: OSI Approved :: GNU Affero General Public License v3
Operating System :: OS Independent
""".format(**SETUP_INFO).strip().splitlines())
SETUP_INFO.update(packages=[
    'whitewall',
    'whitewall.lib',
    'whitewall.lib.whitewall',
    'whitewall.lib.users',
    'whitewall.lib.users.fixtures',
    'whitewall.projects',
    'whitewall.projects.whitewall1',
    'whitewall.projects.whitewall1.tests',
    'whitewall.projects.whitewall1.settings',
    'whitewall.projects.whitewall1.settings.fixtures',
])

SETUP_INFO.update(message_extractors={
    'whitewall': [
        ('**/cache/**', 'ignore', None),
        ('**.py', 'python', None),
        ('**.js', 'javascript', None),
        ('**/config/**.html', 'jinja2', None),
    ],
})

SETUP_INFO.update(package_data=dict())


def add_package_data(package, *patterns):
    l = SETUP_INFO['package_data'].setdefault(package, [])
    l.extend(patterns)
    return l

l = add_package_data('whitewall.lib.whitewall')
for lng in 'en bn'.split():
    l.append('locale/%s/LC_MESSAGES/*.mo' % lng)
