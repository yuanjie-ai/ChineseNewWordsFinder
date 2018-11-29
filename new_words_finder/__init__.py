#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
__title__ = '__init__'
__author__ = 'JieYuan'
__mtime__ = '18-11-29'
"""
from .utils import get_stopwords, Ngrams, get_module_path
from .new_words_finder import NewWordsFinder

data_dir = get_module_path('./data', __file__)
stopwords = get_stopwords(data_dir + '/stopwords.txt')
ng = Ngrams()
