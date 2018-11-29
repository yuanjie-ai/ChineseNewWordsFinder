#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
__title__ = 'setup.py'
__author__ = 'JieYuan'
__mtime__ = '18-11-29'
"""

from setuptools import find_packages, setup

with open("README.md", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='new_words_finder',
    version='1.0.0',
    url='https://github.com/Jie-Yuan/ChineseNewWordsFinder',
    keywords=["DeepLearning", "nlp", "new words"],
    description=('description'),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='JieYuan',
    author_email='313303303@qq.com',
    maintainer='JieYuan',
    maintainer_email='313303303@qq.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['*.*']},
    platforms=["all"],
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],

    # pip install -r requirements.txt
    install_requires=[
        'tqdm',
        'jieba',
    ]
)
