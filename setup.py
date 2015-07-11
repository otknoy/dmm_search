from setuptools import setup

setup(
    name='dmm-search',
    version='0.1.1',
    description="DMM search API for Python",
    py_modules=['dmm'],
    package_dir={'': 'src'},
    keywords='dmm, search',
    author='otknoy',
    author_email='otknoy@gmail.com',
    url='https://github.com/otknoy/dmm_search',
    install_requires=['nkf']
)
