from setuptools import setup
from codecs import open
from os import path


PACKAGE_NAME = 'aws-lambda-rest-api'

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=PACKAGE_NAME,
    version='1.0.12',
    packages=['aws_lambda_rest_api'],
    author='Kohei Okamoto',
    author_email='ohayousagi.ac.kook0727@gmail.com',
    url='https://github.com/Cohey0727/aws-lambda-rest-api',

    description='Generate rest api for lambda like django view.',  # パッケージの簡単な説明
    # long_description=long_description,
    # long_description_content_type='text/markdown',
    keywords='aws lambda rest',  # PyPIでの検索用キーワードをスペース区切りで指定

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    license='MIT',
)
