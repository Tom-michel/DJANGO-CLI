from setuptools import setup, find_packages

setup(
    name='dj-cli',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Click',  # For command-line interface
    ],
    entry_points={
        'console_scripts': [
            'dj-cli=dj_cli.cli:main',
        ],
    },
    description='A CLI for creating Django projects with customizable options',
    author='Michel Btompe (Tom)',
    author_email='michelbtompe@gmail.com',
    url='https://github.com/Tom-michel/DJANGO-CLI',
)
