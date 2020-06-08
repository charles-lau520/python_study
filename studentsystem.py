import os
import re

def menu():
    # 输出菜单
    print("*****学生信息管理系统*****")
    print("---1 录入学生信息")
    print("---2 超找学生信息")
    print("---3 删除学生信息")
    print("---4 修改学生信息")
    print("---5 排序")
    print("---6 统计学生总人数")
    print("---7 显示所有学生信息")
    print("---0 退出系统")
    print("=======================")
    print("说明：通过数字选择菜单")

def insert():
    studentList = []
    mark = True
    while mark:
        id = input("请输入ID（如 1001）：")
        if not id:
            break
        name = input("请输入名字：")
        if not name:
            break
        try:
            english = int(input("请输入英语成绩："))
            python = int(input("请输入Python成绩："))
            c = int(input("请输入C语言成绩:"))
        except Exception as e:
            print("输入无效，不是整型数值......重新录入信息")
            continue
        student = {"id": id,"name": name,"english": english,"python": python,"c": c}
        studentList.append(student)
        inputMark = input("是否继续添加？(y/n)")
        if inputMark == "y":
            mark = True
        else:
            mark = False
    save(studentList)
    print("学生信息录入完毕！！！")
def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r') as rfile:
            student_old = rfile.readlines()
    else:
        return
    studentid = input("请输入要修改的学生ID：")
    with open(filename,'w') as wfile:
        for student in student_old:
            d = dict(eval(student))
            if d["id"] == studentid:
                print("找到了这名学生，可以修改他/她的信息！")
                while True:
                    try:
                        d["name"] = input("请输入姓名：")
                        d["english"] = int(input("请输入英语成绩："))
                        d["python"] = int(input("请输入Python成绩："))
                        d["c"] = int(input("请输入C语言成绩："))
                    except:
                        print("您的输入有误，请重新输入：")
                    else:
                        break
                student = str(d)
                wfile.write(student+"\n")
                print("修改成功！")

            else:
                wfile.write(student)
    mark = input("是否继续修改其他学生信息？(y/n):")
    if mark == "y":
        modify()


def sort():
    pass


def total():
    pass


def show_student(student_query):
    pass



def search():
    mark = True
    student_query = []
    while mark:
        id = ""
        name = ""
        if os.path.exists(filename):
            mode = input("按ID输入1,按姓名输入2：")
            if mode == "1":
                id = input("请输入学生ID：")
            elif mode == "2":
                iname = input("请输入学生姓名：")
            else:
                print("您的输入有误，请重新输入！")
                search()
            with open(filename,'r') as file:
                student = file.readlines()
                for list in student:
                    d = dict(eval(list))
                    if id is not"":
                        if d[id] == id:
                            student_query.append(d)
                        elif name is not "":
                            student_query.append(d)
                show_student(student_query)
                student_query.clear()
                inputMark = input("是否继续查询？(y/n):")
                if inputMark == "y":
                    mark = True
                else:
                    mark = False



def delete():
    mark = True
    while mark:
        studentId = input("请输入要删除的学生ID:")
        if studentId is not "":
            if os.path.exists(filename):    #判断文件是否存在
                with open(filename,'r') as rfile:   #打开文件
                    student_old = rfile.readlines() #读取文件内容
            else:   #否则内容为空
                student_old = []
            ifdel = False
            if student_old:
                with open(filename,'w') as wfile:
                    d = {}
                    for list in student_old:
                        d = dict(eval(list))    #字符串转字典
                        if d['id'] != studentId:
                            wfile.write(str(d) + '\n')
                        else:
                            ifdel = True
                    if ifdel:
                        print("ID为%s的学生信息已被删除..." %studentId)
                    else:
                        print("没有找到ID为%s的学生信息..." %studentId)
        else:
            print("无学生信息")
            break
        show()
        inputMark = input("是否继续删除？(y/n):")
        if inputMark == 'y':
            mark = True
        else:
            mark = False

def show():
    print("待续......")

def save(student):
    try:
        students_txt = open(filename,"a")    # 追加模式打开
    except Exception as e:
        students_txt = open(filename,"w")    # 捕获异常，文件不存在，创建文件并打开
    for info in student:
        students_txt.write(str(info) + "\n") #按行存储，添加换行符
    students_txt.close()    #关闭文件


def main():
    #print("123")
    ctrl = True
    while(ctrl):
        menu()
        option = input("请选择:")
        option_str = re.sub("\D","",option)
        if option_str in ['0','1','2','3','4','5','6','7']:
            option_int = int(option_str)
            if option_int == 0:
                print("您已退出学生信息管理系统！")
                ctrl = False
            elif option_int == 1:
                insert()
            elif option_int == 2:
                search()
            elif option_int == 3:
                delete()
            elif option_int == 4:
                modify()
            elif option_int == 5:
                sort()
            elif option_int == 6:
                total()
            elif option_int == 7:
                show()

if __name__ == '__main__':
    filename = "student.txt"
    main()


