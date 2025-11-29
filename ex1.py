# 超简易学生管理系统
students = []

while True:
    print("="*26)
    print("欢迎使用超简易学生管理系统")
    print("="*26)
    print("1.添加 2.查看 3.删除 4.退出")
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
        if len(students) == 0:
            print("没有学生可以删除！")
        else:
            print("\n所有学生:")
            for i, name in enumerate(students, 1):
                print(f"{i}. {name}")
            try:
                index_to_remove = int(input("请输入要删除的学生的序号: ")) - 1
                if 0 <= index_to_remove < len(students):
                    removed_student = students.pop(index_to_remove)
                    print(f"学生 {removed_student} 已删除！现有 {len(students)} 名学生")
                else:
                    print("输入的序号无效！")
            except ValueError:
                print("请输入一个有效的数字！")
    
    elif choice == "4":
        print("再见！")
        break
    
    else:
        print("输入错误！")
