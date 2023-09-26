import random
from fractions import Fraction
import argparse
import re

correct_count = 0
wrong_count = 0


def readfile(path):
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as file:
            text = file.readlines()
    except:
        print("文件读取错误,请检查文件路径是否正确")
        return False
    return text

def writefile(path,text):
    try:
        with open(path, 'a', encoding='utf-8', errors='ignore') as file:
            file.write(text)
    except:
        print("文件写入错误,请检查文件路径是否正确")
        return False
    return True
def writelinesfile(path,text):
    try:
        with open(path, 'a', encoding='utf-8', errors='ignore') as file:
            file.writelines(text)
    except:
        print("文件写入错误,请检查文件路径是否正确")
        return False
    return True

# 命令行参数

def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, default=None, help='设定生成的题目数量,如-n 10,生成10个运算式子')  # 表达式数量
    parser.add_argument('-r', type=int, default=None, help='设定生成运算数的最大值,如-r 10，生成运算数的最大值为10')  # 最大数值
    parser.add_argument('-e', default=None, help='输入测试文件路径,-e xxx.txt,输入测试文件')  # 测试文件
    parser.add_argument('-a', default=None, help='输入答案文件路径,-a xxx.txt,测试题目的答案')  # 答案文件
    return parser




def correct_answer(exercises_file, answers_file):
    global correct_count, wrong_count
    exercises = readfile(exercises_file)
    answers = readfile(answers_file)
    if exercises == False or answers == False:
        print("文件读取错误,请检查文件路径是否正确")
        return False
    incorrect_questions = []
    correct_questions = []
    for i, (line1, line2) in enumerate(zip(exercises, answers), 1):
        # 正则表达式！！！！！！！
        expression_match = re.match(r'四则运算题目.\d+\t(.*?)=', line1)
        result_match = re.search(r'\t(.*)$', line2)
        if expression_match and result_match:
            expression = expression_match.group(1).strip()
            result = result_match.group(1).strip()
            res = Fraction(eval(expression)).limit_denominator()
            result_end = f"{res.numerator // res.denominator}'{res.numerator % res.denominator}/{res.denominator}" \
                if res.numerator > res.denominator != 1 else str(res)
            if result_end == str(result):
                correct_count += 1
                correct_questions.append(str(i))
            else:
                wrong_count += 1
                incorrect_questions.append(str(i))
    # 清空文件
    open('Grade.txt', 'w').close()
    writefile('Grade.txt',f"Correct: {correct_count} ({', '.join(correct_questions)})\n")
    writefile('Grade.txt',f"Wrong: {wrong_count} ({', '.join(incorrect_questions)})\n")
    print(f"Correct answers: {correct_count},({', '.join(correct_questions)})\n")
    print(f"Wrong answers: {wrong_count},({', '.join(incorrect_questions)})\n")
    print("批改结果已生成,请查看Grade.txt文件")

symbol = ['+', '-', '*', '/']
expressions = set()  # 保存已生成的题目


# 自定义比较函数，判断题目是否重复
def is_duplicate(expression):
    rpn_expression = convert_to_rpn(expression)
    return rpn_expression in expressions


# 将中缀表达式转换为逆波兰表达式
def convert_to_rpn(expression):
    stack = []
    rpn = []
    for token in expression:
        if token in symbol:
            while stack and stack[-1] in symbol and symbol.index(stack[-1]) >= symbol.index(token):
                rpn.append(stack.pop())
            stack.append(token)
        else:
            rpn.append(token)
    while stack:
        rpn.append(stack.pop())
    return tuple(rpn)  # 返回元组以便比较


def generate_expression(num_operators, scope):
    if num_operators == 0:
        num = random.randint(1, scope-1)
        return str(num)
    else:
        operator = random.choice(symbol)
        num1 = generate_expression(num_operators - 1,scope)
        num2 = generate_expression(num_operators - 1,scope)

        expression = f"{num1} {operator} {num2}"
        if random.choice([True, False]):
            expression = f"({expression})"
        return expression
def printhelp():
    print("参数输入错误,请检查参数是否输入正确")
    cer1 = input()
    print("是否需要帮助信息，以及了解相关命令参数的使用?(y|n)")
    cer2 = input()
    if cer1 == 'Y' or cer1 == 'y':
        parser.print_help()
        print("输入的测试文件格式要求:与项目生成的文件格式一致，如四则运算题目.1 ... 以及输入答案文件格式也要统一如:第1题的答案: ...")
    if cer2 == 'Y' or cer2 == 'y':
        parser.print_help()
        print("输入的测试文件格式要求:与项目生成的文件格式一致，如四则运算题目.1 ... 以及输入答案文件格式也要统一如:第1题的答案: ...")

def create_exercise(subject_num, scope):
    # 清空文件
    open('Exercises.txt', 'w').close()
    open('Answers.txt', 'w').close()
    i = 0
    while i < subject_num:
        expression = generate_expression(2, scope)  # 生成带括号的表达式，最多两个运算符
        expression_str = expression

        try:
            result = eval(expression_str)  # 题目答案
        except ZeroDivisionError:
            continue  # 如果除数为零，则重新生成下一个题目

        if result < 0 or is_duplicate(expression):
            continue  # 如果结果小于0或者题目已存在，则重新生成下一个题目

        expressions.add(convert_to_rpn(expression))  # 将题目添加到集合中
        i += 1

        # 用with语句进行操作
        writelinesfile('Exercises.txt',f'四则运算题目.{i}\t{expression_str}=\n')
        res = Fraction(eval(expression)).limit_denominator()
        result_end = f"{res.numerator // res.denominator}'{res.numerator % res.denominator}/{res.denominator}" \
            if res.numerator > res.denominator != 1 else str(res)
        writelinesfile('Answers.txt',f'第{i}题的答案：\t{result_end}\n')
    print("题目已生成,请查看Exercises.txt和Answers.txt文件")

def findnotnone(num):
    if num != None:
        return True
    else:
        return False
def  test(num1,text1):
    num2 = 10
    if (findnotnone(num1)):
        if num1 <= 0:
            print("参数输入错误,请检查参数是否输入正确")
            exit()
        else:
            num2 = num1
    else:
        print(text1)
    return num2
if __name__ == "__main__":
    # 读取命令行参数
    try:
        parser = argparser()

        options, argv_rest = parser.parse_known_args()
        # 测试用例
        # options.n=100
        # options.r=100
        # options.e="Exercises.txt"
        # options.a="Answers.txt"
        if options.n != None or options.r != None and options.e == None and options.a == None:
            subject_num = test(options.n, "题目数量未指定，默认为10")
            scope = test(options.r, "运算数最大值未指定，默认为10")
            create_exercise(subject_num, scope)
        elif options.n == None and options.r == None and options.e != None and options.a != None:
            exercises_file = options.e
            answers_file = options.a
            print(exercises_file)
            print(answers_file)
            correct_answer(exercises_file, answers_file)
        else:
            printhelp()
    except:
        printhelp()


