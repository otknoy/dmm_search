from setuptools import setup

setup(
    name='dmm-search',
    version='0.0.1',
    description="DMM search API",
    py_mdules=['dmm'],
    package_dir={'': 'src'},
    author='otknoy',
    author_email='otknoy@gmail.com',
    url='https://github.com/otknoy/dmm_search_api',
    install_requires=['nkf']
)
