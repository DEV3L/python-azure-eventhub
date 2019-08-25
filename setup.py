from setuptools import setup, find_packages

requirements = []

with open('requirements.txt') as file:
    for line in file:
        if line:
            requirements.append(line)

setup(
    name='python-azure-eventhub',
    packages=find_packages(),
    version='0.1',
    description='Python Hello World example of Microsoft Azure Event Hub.',
    author='Justin Beall',
    author_email='jus.beall@gmail.com',
    keywords=['dev3l', 'python', 'azure', 'eventhub'],
    install_requires=requirements,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'],
)
