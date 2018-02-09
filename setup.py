from setuptools import setup, find_packages


version = '1.0.0'

setup(
    name='alex-py',
    version=version,
    description='Alex executes your python scripts with test cases embedded',
    long_description=open('README.rst').read(),
    author='Kaushik Varanasi',
    author_email ='kaushik.varanasi1@gmail.com',
    license='MIT',
    keywords=['Python' ,'Competetive Programming' ,'Test cases' ,'command line', 'cli'],
    url='http://github.com/kaushik94/alex',
    packages=find_packages(),
    package_data={
        'alex': ['*.gitignore']
    },
    install_requires=[
        'docopt>=0.6.1',
        'future'
    ],
    entry_points={
        'console_scripts': [
            'alex=Alex.alex:main'
        ],
    }
)
