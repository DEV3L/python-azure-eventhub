from setuptools import setup, find_packages

setup(
    name='python-azure-etl',
    packages=find_packages(),
    version='0.1',
    description='Python Hello World example of ETL Pipeline using Microsoft Azure.',
    author='Justin Beall',
    author_email='jus.beall@gmail.com',
    keywords=['dev3l', 'python', 'azure', 'eventhub', 'etl'],
    install_requires=[
        'pytest',
        'azure-eventhub',
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'],
)