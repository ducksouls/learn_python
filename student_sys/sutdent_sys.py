'''
@Description: 控制台学生管理系统
@Author: lai
@Date: 2019-08-26 22:40:05
@LastEditTime: 2019-08-30 01:09:12
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
        id = input("请输入学号:")
        if not id:# if not id is None, if id is None都可以
            print("格式有误---请重新输入")
            continue
        name = input("请输入名字:")
        if not name:
            print("格式有误---请重新输入")
            continue
        try:
            chinese = int(input("请输入语文成绩："))
            math = int(input("请输入数学成绩："))
            english = int(input("请输入英语成绩："))
        except:
            print("格式有误---请输入整数")
            continue
        stu_list.append({'id' : id, 'name' : name,'chinese':chinese,'math' : math,'english':english})
        yes_no = input("是否要继续录入学生信息（y/n）?: ")
        if yes_no == 'y' :
            pass
        else:
            mark = False
        #print(stu_list)
    save2file(stu_list)
    

def save2file(stu_list):
    with open('stu.info','a+',encoding="utf-8") as file:
        keys = list(stu_list[0].keys())
        stu_infos = []
        for stu in stu_list:
            values = list(stu.values())
            str1 = r': %s , '.join(keys)
            str2 =str1 +  r': %s'
            str3 = str2 % tuple(values)
            stu_infos.append(str3+'\n')
        # 不会自动换行。。。
        file.writelines(stu_infos)
        

    
# def search():


# def detele():


# def modify():


# def sort():


# def total():


# def show():


# def show_stu():


if __name__ == "__main__":
    insert()
