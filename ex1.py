# 超简易学生管理系统
students = []

while True:
    print("===========================")
    print("欢迎使用超简易学生管理系统")
    print("===========================")
    print("1.添加 2.查看 3.退出")
    choice = input("请选择: ")
    
    if choice == "1":
        name = input("输入姓名: ")
        students.append(name)
        print(f"添加成功！现有{len(students)}名学生")
    
    elif choice == "2":
        print("\n所有学生:")
        for i, name in enumerate(students, 1):
            print(f"{i}. {name}")
    
    elif choice == "3":
        print("再见！")
        break
    
    else:
        print("输入错误！")
