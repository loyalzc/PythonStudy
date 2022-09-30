# !/usr/bin/python
# -*- coding: utf8 -*-
"""
 Package：
 User：loyal
 Date：2022/9/29
 Dscription：
"""
import random

student_names = ['A', 'B', 'C', 'D', 'E']
suject_names = ['1', '2', '3', '4', '5']

class_score = {}
for std in student_names:
    std_score = {}
    for suj in suject_names:
        std_score[suj] = random.randint(0,100)
    class_score[std] = std_score


def get_student_score(std_name, suj_name):
    """
    获取某个学生某个科目的成绩
    :param std_name: 学生名字
    :param suj_name: 科目名字
    :return: 得分
    """
    score = class_score[std_name][suj_name]
    return score


def get_student_rank(class_score):
    """
    计算所有学生的总分并排序输出
    :param class_score: 各个学生各个科目分数
    :return: 按照总分由大到小的顺序排序 姓名和总分
    """
    rank_score = {}
    return rank_score



def set_student_info(class_score):
    """
    新增 学生的 年龄（0-20 随机） 性别（M F 随机）
    :param class_score: 原学生信息
    :return: 原来字典新增后的学生信息 包括（年龄 性别 各个科目分数
    """
    return class_score


print(get_student_score('A', '2'))
import random

student_names = ['A', 'B', 'C', 'D', 'E']
suject_names = ['1', '2', '3', '4', '5']

class_score = {}
for std in student_names:
    std_score = {}
    for suj in suject_names:
        std_score[suj] = random.randint(0,100)
    class_score[std] = std_score


student_sum1 = {}
for name1 in class_score[student_names]:
               result = 0
            for name2 in student_names[subject_names]:
                result = result + name2
            student_sum1[name1] = result

rank_score = sorted(student_sum1.items(), key=lambda x: x[1], reverse=true)



def get_student_rank(class_score):
    """
    计算所有学生的总分并排序输出
    :param class_score: 各个学生各个科目分数
    :return: 按照总分由大到小的顺序排序 姓名和总分
    """
    rank_score = {}
    return rank_score

print(rank_score)
