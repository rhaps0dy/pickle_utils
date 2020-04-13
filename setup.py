from distutils.core import setup

setup(
    name = 'pickle_utils',
    packages = ['pickle_utils'],
    version = '0.1.1',
    description = '(use pandas.read_pickle and pandas.to_pickle instead) Memoize functions to disk, load and save compressed Pickle files.',
    author = 'Adrià Garriga-Alonso',
    author_email = 'adria.garriga@gmail.com',
    url = 'https://github.com/rhaps0dy/pickle_utils',
    download_url = 'https://github.com/rhaps0dy/pickle_utils/archive/0.2.tar.gz',
    keywords = ['pickle'], # arbitrary keywords
    classifiers = [],
    install_requires=["pandas>=1.0"],
)
