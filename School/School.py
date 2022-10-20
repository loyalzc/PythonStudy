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
        std_score[suj] = random.randint(0, 100)
    class_score[std] = std_score

"""

class_score_02 = dict(class_score)
for std in student_names:
    result = 0
    for suj in subject_names:
        result = result + class_score_02[std][suj]
    class_score_02[std] = result
class_score_03 = dict(class_score)


    pass
"""


random.randint(0, 20)
random.choice(['M', 'F'])

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
    # rank_sort = sorted(class_score_02.item(), key=lambda x: x[1], reverse=true)
    for std_name, subj_scores in class_score.items():
        sum_socre = 0
        for suj, score in subj_scores.items():
            sum_socre += score
        subj_scores["sum_socre"] = sum_socre
    print(class_score)

def set_student_info(class_score):
    """
    新增 学生的 年龄（0-20 随机） 性别（M F 随机）
    :param class_score: 原学生信息
    :return: 原来字典新增后的学生信息 包括（年龄 性别 各个科目分数
    """
    for std_name, stf_info in class_score.items():
        stf_info['age'] = random.randint(0, 20)
        stf_info['gender'] = random.choice(['M', 'F'])
    return class_score

    #如何评价我的代码，哪错了，不能这样遍历吗
def set_student_info(class_score):
    """
    新增 学生的 年龄（0-20 随机） 性别（M F 随机）
    :param class_score: 原学生信息
    :return: 原来字典新增后的学生信息 包括（年龄 性别 各个科目分数
    """
    for k in class_socre:
        class_socre[k][gender] = random.choice(['M', 'F'])
        class_socre[k][age] = random.randint(0, 20)
    return class_score

def get_student_info(file_path):
    """
    从文件获取学生的信息
    :param file_path:文件路径
    :return: 学生信息字典
    """
    student_dict = {}

    return student_dict

print(get_student_score('A', '2'))
print(get_student_rank(class_score))
print(set_student_info(class_score))



