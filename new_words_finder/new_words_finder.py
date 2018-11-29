#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'new_words_finder'
__author__ = 'JieYuan'
__mtime__ = '18-11-29'
"""
import os
import jieba

jieba.enable_parallel(4)
jieba.lcut("分词测试")
from tqdm import tqdm
from .trie import TrieNode
from .utils import get_stopwords, load_dictionary, Ngrams, save_model, load_model, get_module_path


class NewWordsFinder(object):

    def __init__(self, corpus):
        self.corpus = corpus
        self.root = None
        self.ng = Ngrams()
        self.data_dir = get_module_path('./data', __file__)
        self.stopwords = get_stopwords(self.data_dir + '/stopwords.txt')
        self.__root_init()
        self.__load_data()

    def get_new_words(self, top_n=5):
        return self.root.find_word(top_n)[1]  # result, add_words

    def __root_init(self):
        root_name = self.data_dir + "/root.pkl"
        if os.path.exists(root_name):
            self.root = load_model(root_name)
        else:
            dict_name = self.data_dir + '/dict.txt'
            word_freq = load_dictionary(dict_name)
            self.root = TrieNode('*', word_freq)
            save_model(self.root, root_name)

    def __load_data(self):
        """插入节点"""

        with open(self.corpus) as f:
            for line in tqdm(f, "Loading Corpus ..."):
                word_list = [x for x in jieba.cut(line.strip(), cut_all=False) if x not in self.stopwords]
                ngrams = self.ng.everygrams(word_list, max_len=3)
                for d in ngrams:
                    self.root.add(d)


if __name__ == '__main__':
    nwf = NewWordsFinder('./demo.txt')
    print(nwf.get_new_words())
