'''
@Description: 控制台学生管理系统
@Author: lai
@Date: 2019-08-26 22:40:05
@LastEditTime: 2019-09-03 00:02:22
@LastEditors: Please set LastEditors
'''

import re
import os
'''
学生信息：id ，名字， 语数英的成绩
'''
filename = "stu.info"

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
    ctrl = True  # 标记是否退出系统
    while (ctrl):
        menu()  # 显示菜单
        option = input("请选择：")  # 选择菜单项
        option_str = re.sub("\D", "", option)  # 提取数字
        if option_str in ['0', '1', '2', '3', '4', '5', '6', '7']:
            option_int = int(option_str)
            if option_int == 0:  # 退出系统
                print('您已退出学生成绩管理系统！')
                ctrl = False
            elif option_int == 1:  # 录入学生成绩信息
                insert()
            elif option_int == 2:  # 查找学生成绩信息
                search()
            elif option_int == 3:  # 删除学生成绩信息
                delete()
            elif option_int == 4:  # 修改学生成绩信息
                modify()
            elif option_int == 5:  # 排序
                sort()
            elif option_int == 6:  # 统计学生总数
                total()
            elif option_int == 7:  # 显示所有学生信息
                show()
    

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
        # keys = list(stu_list[0].keys())
        # stu_infos = []
        for stu in stu_list:
            # values = list(stu.values())
            # str1 = r': %s , '.join(keys)
            # str2 =str1 +  r': %s'
            # str3 = str2 % tuple(values)
            # stu_infos.append(str3+'\n')
            file.write(str(stu) + '\n')
        file.close()
        

# 这个方法相当不优雅
def search():
    with open('stu.info', 'r') as file:
        mark = True
        re_stus = []
        while mark :
            print("请选择搜索模式---mod：")
            mod = input('1---按学号搜索，2---按姓名搜索：')
            if mod == '1':
                stus = file.readlines()
                input_id = input('请输入学号：')
                for s in stus:
                    sdic = dict(eval(s))# 字符串转dict---需要字符串具有字典格式{a:b,c:d}
                    if sdic['id'] == input_id:
                        re_stus.append(sdic)
                if len(re_stus) > 0 :
                    print(re_stus)
                    a = input('是否继续y/n')
                    if a == 'y':
                        re_stus.clear()
                        file.seek(0)
                        continue
                    mark = False
                    break
                else:
                    print('没有查询到该生信息，或者输入有误')
                    flag = input('是否继续（y/n）')
                    if flag == 'y':
                        re_stus.clear()
                        file.seek(0)
                        continue
                    else:
                        break
            elif mod == '2':
                stus = file.readlines()
                input_name = input('请输入姓名：')
                for s in stus:
                    sdic = dict(eval(s))# 字符串转dict---需要字符串具有字典格式{a:b,c:d}
                    if sdic['name'] == input_name:
                        re_stus.append(sdic)
                if len(re_stus) > 0 :
                    print(re_stus)
                    a = input('是否继续y/n')
                    if a == 'y':
                        re_stus.clear()
                        file.seek(0)
                        continue
                    mark = False
                    break
                else:
                    print('没有查询到该生信息，或者输入有误')
                    flag = input('是否继续（y/n）')
                    if flag == 'y':
                        re_stus.clear()
                        file.seek(0)
                        continue
                    else:
                        break
            else:
                print('输入有误---请重新输入')
                continue
            
        # 读过一次后再读将会所读成空。。。
        # stus1 = file.readlines()
        # print(stus)
        # print(stus1) # out: []
        

def delete():
    mark = True  # 标记是否循环
    while mark:
        studentId = input("请输入要删除的学生ID：")
        if studentId is not "":  # 判断要删除的学生是否存在
            if os.path.exists(filename):  # 判断文件是否存在
                with open(filename, 'r') as rfile:  # 打开文件
                    student_old = rfile.readlines()  # 读取全部内容
            else:
                student_old = []
            ifdel = False  # 标记是否删除
            if student_old:  # 如果存在学生信息
                with open(filename, 'w') as wfile:  # 以写方式打开文件
                    d = {}  # 定义空字典
                    for list in student_old:
                        d = dict(eval(list))  # 字符串转字典
                        if d['id'] != studentId:
                            wfile.write(str(d) + "\n")  # 将一条学生信息写入文件
                        else:
                            ifdel = True  # 标记已经删除
                    if ifdel:
                        print("ID为 %s 的学生信息已经被删除..." % studentId)
                    else:
                        print("没有找到ID为 %s 的学生信息..." % studentId)
            else:  # 不存在学生信息
                print("无学生信息...")
                break  # 退出循环
            show()  # 显示全部学生信息
            inputMark = input("是否继续删除？（y/n）:")
            if inputMark == "y":
                mark = True  # 继续删除
            else:
                mark = False  # 退出删除学生信息功能


'''4 修改学生成绩信息'''


def modify():
    show()  # 显示全部学生信息
    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, 'r') as rfile:  # 打开文件
            student_old = rfile.readlines()  # 读取全部内容
    else:
        return
    studentid = input("请输入要修改的学生ID：")
    with open(filename, "w") as wfile:  # 以写模式打开文件
        for student in student_old:
            d = dict(eval(student))  # 字符串转字典
            if d["id"] == studentid:  # 是否为要修改的学生
                print("找到了这名学生，可以修改他的信息！")
                while True:  # 输入要修改的信息
                    try:
                        d["name"] = input("请输入姓名：")
                        d["english"] = int(input("请输入英语成绩："))
                        d["python"] = int(input("请输入Python成绩："))
                        d["c"] = int(input("请输入C语言成绩："))
                    except:
                        print("您的输入有误，请重新输入。")
                    else:
                        break  # 跳出循环
                student = str(d)  # 将字典转换为字符串
                wfile.write(student + "\n")   # 将修改的信息写入到文件
                print("修改成功！")
            else:
                wfile.write(student)  # 将未修改的信息写入到文件
    mark = input("是否继续修改其他学生信息？（y/n）：")
    if mark == "y":
        modify()  # 重新执行修改操作


'''5 排序'''


def sort():
    show()  # 显示全部学生信息
    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, 'r') as file:  # 打开文件
            student_old = file.readlines()  # 读取全部内容
            student_new = []
        for list in student_old:
            d = dict(eval(list))  # 字符串转字典
            student_new.append(d)  # 将转换后的字典添加到列表中
    else:
        return
    ascORdesc = input("请选择（0升序；1降序）：")
    if ascORdesc == "0":  # 按升序排序
        ascORdescBool = False           # 标记变量，为False表示升序排序
    elif ascORdesc == "1":  # 按降序排序
        ascORdescBool = True          # 标记变量，为True表示降序排序
    else:
        print("您的输入有误，请重新输入！")
        sort()  
    mode = input("请选择排序方式（1按语文成绩排序；2按数学成绩排序；3按英语成绩排序；0按总成绩排序）：")
    if mode == "1":  # 按英语成绩排序
        student_new.sort(key=lambda x: x["english"], reverse=ascORdescBool)
    elif mode == "2":  # 按Python成绩排序
        student_new.sort(key=lambda x: x["python"], reverse=ascORdescBool)
    elif mode == "3":  # 按C语言成绩排序
        student_new.sort(key=lambda x: x["c"], reverse=ascORdescBool)
    elif mode == "0":  # 按总成绩排序
        student_new.sort(key=lambda x: x["english"] + x["python"] + x["c"], reverse=ascORdescBool)
    else:
        print("您的输入有误，请重新输入！")
        sort()
    show_student(student_new)  # 显示排序结果


''' 6 统计学生总数'''


def total():
    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, 'r') as rfile:  # 打开文件
            student_old = rfile.readlines()  # 读取全部内容
            if student_old:
                print("一共有 %d 名学生！" % len(student_old))
            else:
                print("还没有录入学生信息！")
    else:
        print("暂未保存数据信息...")


''' 7 显示所有学生信息 '''


def show():
    student_new = []
    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, 'r') as rfile:  # 打开文件
            student_old = rfile.readlines()  # 读取全部内容
        for list in student_old:
            student_new.append(eval(list))  # 将找到的学生信息保存到列表中
        if student_new:
            show_student(student_new)
    else:
        print("暂未保存数据信息...")


# 将保存在列表中的学生信息显示出来
def show_student(studentList):
    if not studentList:
        print("(o@.@o) 无数据信息 (o@.@o) \n")
        return
    format_title = "{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}"
    print(format_title.format("ID", "名字", "语文成绩", "数学成绩", "英语成绩", "总成绩"))
    format_data = "{:^6}{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}"
    for info in studentList:
        print(format_data.format(info.get("id"), info.get("name"), str(info.get("chinese")), str(info.get("math")),
                                str(info.get("english")),
                                str(info.get("english") + info.get("chinese") + info.get("math")).center(12)))



if __name__ == "__main__":
    main()
