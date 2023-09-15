# -*- coding: UTF-8 -*-

from os import error
from random import random
from json import dumps, loads

# 生成随机数文件
class RandomArray:
    def dump_random_array(file='numbers.json', size=10 ** 4):
        fo = open(file, 'w', 1024)
        numlst = list()
        for i in range(size):
            numlst.append(int(random() * 10 ** 10))
        fo.write(dumps(numlst))
        fo.close()


    # 加载随机数列表
    def load_random_array(file='numbers.json'):
        fo = open(file, 'r', 1024)
        try:
            numlst = fo.read()
        finally:
            fo.close()
        return loads(numlst)

class EnhancedArray:
    # Remove duplicate list
    def distinct_list(sourcelist):
        try:
            if len(sourcelist) ==0:
                return []
            print("Length of original list ：", len(sourcelist))
            sourcelist = set(map(tuple,sourcelist))  #need to convert the inner lists to tuples so they are hashable
            sourcelist = list(map(list,sourcelist)) #Now convert tuples back into lists (maybe unnecessary?)
            print("Length of filtered list : ", len(sourcelist))

# Another method to filter
#            b_set = set(tuple(x) for x in a)
#            b = [ list(x) for x in b_set ]
        except Exception as e: 
            print(e)
            return []
        return sourcelist