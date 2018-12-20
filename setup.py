from setuptools import setup, find_packages

setup(
    name='hep-data-backends',
    version='0.4.0',
    url='https://github.com/wonderlandcompute/hep-data-backends',
    author='Alexander Baranov && Musinov Igor',
    author_email='sashab1@yandex-team.ru',
    packages=find_packages(),
    description='HEP backends',
    install_requires=[
        "requests>=2.5.1",
        "gitpython",
        "sh",
        "boto3",
    ]
)
