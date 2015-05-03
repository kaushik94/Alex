from setuptools import setup, find_packages


version = '1.0.0'

setup(
    name='alex',
    version=version,
    description='alex executes your python scripts with test cases embedded',
    long_description=open('README.rst').read(),
    author='Kaushik Varanasi',
    license='MIT',
    keywords=['gitignore', 'git', 'github', 'command line', 'cli'],
    url='http://github.com/kaushik94/alex',
    packages=find_packages(),
    package_data={
        'joe': ['*.gitignore']
    },
    install_requires=[
        'docopt>=0.6.1',
    ],
    entry_points={
        'console_scripts': [
            'alex=Alex.alex:main'
        ],
    }
)
