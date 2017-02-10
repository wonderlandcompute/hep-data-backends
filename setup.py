from setuptools import setup, find_packages

setup(
    name='hep-data-backends',
    version='0.1.0',
    url='https://github.com/skygrid/hep-data-backends',
    author='Alexander Baranov',
    author_email='sashab1@yandex-team.ru',
    packages=find_packages(),
    description='HEP backends',
    install_requires=[
        "requests>=2.5.1",
        "easywebdav-dcache==1.2.4", # fixed easywebdav, see https://github.com/amnong/easywebdav/pull/37
        "gitpython",
        "sh>=1.11",
    ]
)
