# -*- coding: utf-8 -*-
"""
Created on Tue Nov 07 19:18:52 2017

@author: bianl
"""


import numpy as np

def load_data(filename):
    '''
    function：读取包含样本特征和标签的输入文件
    input:filename(str):输入文件名
    output:x_feature(mat):样本特征
           y_label(mat):样本标签
    '''
    x_feature=[]
    y_label=[]
    
    f=open(filename)
    for line in f.readlines():  # 读取每一行数据
        lines=line.strip().split('\t')
        
        #  创建 m*n 的feature矩阵
        x_feature_tmp=[]
        x_feature_tmp.append(1)  # x0的值默认为1
        for i in xrange(len(lines)-1):
            x_feature_tmp.append(float(lines[i]))
        x_feature.append(x_feature_tmp)
                    
        #  创建 1*m 的label矩阵
        y_label.append(float(lines[-1]))
        
    f.close()
    return np.mat(x_feature),np.mat(y_label).T  #label矩阵的转置 m*1



def lr_train(alpha,maxcycle,feature,label):
    
    
        
        
        
feature,label=load_data('data.txt')