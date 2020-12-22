import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

if not os.path.exists('ehf_invoice/VERSION'):
    version = '0'
else:
    with open('ehf_invoice/VERSION', 'r') as fp:
        version = fp.read().strip()
        version = version[1:]  # Remove v before version number

setup(
    name='django-ehf-import',
    version=version,
    packages=find_packages(),
    include_package_data=True,
    license='GPL',
    description='A django app to load EHF invoices into a database',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/StorFollo-IKT/django-ad-import',
    author='Anders Birkenes',
    author_email='anders.birkenes@storfolloikt.no',
    classifiers=[
        'Framework :: Django',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: '
        'GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=['django>=2,<4'],
)
