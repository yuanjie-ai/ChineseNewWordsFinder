# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/26 下午5:20
# @Author  : zhanzecheng
# @File    : utils.py
# @Software: PyCharm
"""
import os
import pickle
from itertools import chain, combinations

get_module_path = lambda path, file: os.path.normpath(os.path.join(os.getcwd(), os.path.dirname(file), path))


def get_stopwords(path):
    with open(path) as f:
        return {line.strip() for line in f}


def generate_ngram(input_list, n):
    result = []
    for i in range(1, n + 1):
        result.extend(zip(*[input_list[j:] for j in range(i)]))
    return result


def load_dictionary(filename):
    """加载外部词频记录"""
    word_freq = {}
    print('------> 加载外部词频')
    with open(filename, 'r') as f:
        for line in f:
            try:
                line_list = line.strip().split(' ')
                # 规定最少词频
                if int(line_list[1]) > 2:
                    word_freq[line_list[0]] = line_list[1]
            except IndexError as e:
                print(line)
                continue
    return word_freq


def save_model(model, filename):
    with open(filename, 'wb') as fw:
        pickle.dump(model, fw)


def load_model(filename):
    with open(filename, 'rb') as fr:
        model = pickle.load(fr)
    return model





class Ngrams(object):
    def __init__(self):
        pass

    def pad_sequence(self, sequence, n, pad_left=False, pad_right=False,
                     left_pad_symbol=None, right_pad_symbol=None):

        sequence = iter(sequence)
        if pad_left:
            sequence = chain((left_pad_symbol,) * (n - 1), sequence)
        if pad_right:
            sequence = chain(sequence, (right_pad_symbol,) * (n - 1))
        return sequence

    # add a flag to pad the sequence so we get peripheral ngrams?

    def ngrams(self, sequence, n, pad_left=False, pad_right=False,
               left_pad_symbol=None, right_pad_symbol=None):

        sequence = self.pad_sequence(sequence, n, pad_left, pad_right,
                                     left_pad_symbol, right_pad_symbol)

        history = []
        while n > 1:
            history.append(next(sequence))
            n -= 1
        for item in sequence:
            history.append(item)
            yield tuple(history)
            del history[0]

    def bigrams(self, sequence, **kwargs):


        for item in self.ngrams(sequence, 2, **kwargs):
            yield item

    def trigrams(self, sequence, **kwargs):


        for item in self.ngrams(sequence, 3, **kwargs):
            yield item

    def everygrams(self, sequence, min_len=1, max_len=-1, **kwargs):

        if max_len == -1:
            max_len = len(sequence)
        for n in range(min_len, max_len + 1):
            for ng in self.ngrams(sequence, n, **kwargs):
                yield ng
