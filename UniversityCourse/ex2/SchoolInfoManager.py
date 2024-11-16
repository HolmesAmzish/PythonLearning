class Person:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def printInfo(self):
        print(f"姓名: {self.name}, 性别: {self.sex}, 年龄: {self.age}")


class Student(Person):
    count = 0  # 静态属性，用于统计学生人数

    def __init__(self, name, sex, age, classes, studentID, scores):
        super().__init__(name, sex, age)
        self.classes = classes
        self.studentID = studentID
        self.scores = scores
        Student.count += 1  # 学生人数自增

    def printInfo(self):
        super().printInfo()  # 调用父类的printInfo方法
        print(f"班级: {self.classes}, 学号: {self.studentID}, 成绩: {self.scores}")

    def __del__(self):
        Student.count -= 1  # 学生人数自减


class Teacher(Person):
    def __init__(self, name, sex, age, department, teacherID, course, salary):
        super().__init__(name, sex, age)
        self.department = department
        self.teacherID = teacherID
        self.course = course
        self.__salary = salary  # 私有属性

    def printInfo(self):
        super().printInfo()  # 调用父类的printInfo方法
        print(f"部门: {self.department}, 工号: {self.teacherID}, 讲授课程: {', '.join(self.course)}")

    def getSalary(self):
        """提供获取私有薪水的方法"""
        return self.__salary


# 创建学生对象
student1 = Student("张三", "男", 18, "高一", 1001, {"语文": 90, "数学": 85, "英语": 88})
student2 = Student("李四", "女", 19, "高二", 1002, {"语文": 92, "数学": 87, "英语": 90})

# 创建教师对象
teacher1 = Teacher("王老师", "男", 35, "数学组", 2001, ["数学", "物理"], 6000)

# 输出学生和教师的信息
print("学生信息：")
student1.printInfo()
student2.printInfo()

print("\n教师信息：")
teacher1.printInfo()

# 输出学生总人数
print(f"\n当前学生总人数: {Student.count}")
