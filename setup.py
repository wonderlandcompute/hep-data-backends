from setuptools import setup, find_packages

setup(
    name='hep-data-backends',
    version='0.2.1',
    url='https://github.com/skygrid/hep-data-backends',
    author='Alexander Baranov',
    author_email='sashab1@yandex-team.ru',
    packages=find_packages(),
    description='HEP backends',
    install_requires=[
        "requests>=2.5.1",
        "easywebdav", # fixed easywebdav, see https://github.com/amnong/easywebdav/pull/37
        "gitpython",
        "sh>=1.11",
    ]
)
