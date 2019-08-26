'''
@Description: 控制台学生管理系统
@Author: lai
@Date: 2019-08-26 22:40:05
@LastEditTime: 2019-08-27 00:24:31
@LastEditors: Please set LastEditors
'''

import re
import os
'''
学生信息：id ，名字， 语数英的成绩
'''
filename = "stu_info"

#输出系统的主界面
def menu():
    print('''
                    学生信息管理系统

    =============== 功能菜单  =============

    1 录入学生信息                         
    2 查找学生信息                         
    3 删除学生信息                         
    4 修改学生信息                         
    5 排序                                 
    6 统计学生总人数                       
    7 显示所有学生信息                     
    0 退出系统
    ========================================      
    
    ''')


def main():
    pass

def insert():
    stu_list = []
    mark = True
    while mark:
        id = input("请输入学号")
        if not id:# if not id is None, if id is None都可以
            print("格式有误---请重新输入")
            break
        name = input("请输入名字")
        if not name:
            print("格式有误---请重新输入")
            break
        try:
            chinese = int(input("请输入语文成绩："))
            math = int(input("请输入数学成绩："))
            english = int(input("请输入英语成绩："))
        except:
            print("格式有误---请输入整数")
            continue
        stu_list.append({'id' : id, 'name' : name,'chinese':chinese,'math' : math,'english':english})
        yes_no = input("是否要继续录入学生信息（y/n）?")
        if yes_no == 'y' :
            pass
        else:
            mark = False
        print(stu_list)


# def save2file():


# def search():


# def detele():


# def modify():


# def sort():


# def total():


# def show():


# def show_stu():


if __name__ == "__main__":
    insert()
