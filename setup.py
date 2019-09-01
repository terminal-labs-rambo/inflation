import sys
if sys.version_info.major < 3:
    sys.exit('Python 3 required but lower version found. Aborted.')

from setuptools import setup, find_packages

setup(
    name='inflation',
    version='0.0.1.dev',
    description='Clusters',
    url='https://github.com/terminal-labs/inflation',
    author='Terminal Labs',
    author_email='solutions@terminallabs.com',
    license=license,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'click',
        'pyyaml',
    ],
    entry_points='''
        [console_scripts]
        inflation=inflation.cli:main
     '''
)
