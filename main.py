# import random
# from fractions import Fraction
# #清除文件内容
# file_handle1 = open('Exercises.txt', 'w+')
# file_handle2 = open('Answers.txt', 'w+')
# file_handle1.close()
# file_handle2.close()
# subject_num = 100  # 题目数量
# scope = 10  # 随机数范围
#
# symbol = ['+', '-', '*', '/']
# expressions = set()  # 保存已生成的题目
#
#
# # 自定义比较函数，判断题目是否重复
# def is_duplicate(expression):
#     rpn_expression = convert_to_rpn(expression)
#     return rpn_expression in expressions
#
#
# # 将中缀表达式转换为逆波兰表达式
# def convert_to_rpn(expression):
#     stack = []
#     rpn = []
#     for token in expression:
#         if token in symbol:
#             while stack and stack[-1] in symbol and symbol.index(stack[-1]) >= symbol.index(token):
#                 rpn.append(stack.pop())
#             stack.append(token)
#         else:
#             rpn.append(token)
#     while stack:
#         rpn.append(stack.pop())
#     return tuple(rpn)  # 返回元组以便比较
#
#
# i = 0
# while i < subject_num:
#     num1 = random.randint(1, scope)
#     num2 = random.randint(1, scope)
#     num3 = random.randint(1, scope)
#
#     n1 = random.randint(1, 3)
#     n2 = random.randint(1, 3)
#
#     char_num = random.randint(1, 3)  # 使运算符的个数不大于三个
#     if char_num == 1:
#         expression = (str(num1), symbol[n1], str(num2))
#     else:
#         expression = (str(num1), symbol[n1], str(num2), symbol[n2], str(num3))
#     expression_str = ' '.join(expression)
#
#     result = eval(expression_str)  # 题目答案
#     if result < 0 or is_duplicate(expression):
#         continue  # 如果结果小于0或者题目已存在，则重新生成下一个题目
#
#     expressions.add(convert_to_rpn(expression))  # 将题目添加到集合中
#     i += 1
#
#     file_handle1 = open('Exercises.txt', 'a', encoding='utf-8')  # 写入题目
#     file_handle1.writelines('四则运算题目.' + str(i) + '\t' + expression_str + '=' + '\n')
#     file_handle1.close()
#
#     result = Fraction(result).limit_denominator()  # 结果转化为近似分数
#     w = result.numerator
#     r = result.denominator
#     if w > r != 1:  # 判断是否为带分数
#         result_end = str(str(int(w / r)) + "'" + str(w % r) + "/" + str(r))  # 转化为带分数形式
#     else:
#         result_end = str(result)
#
#     file_handle2 = open('Answers.txt', 'a', encoding='utf-8')  # 写入答案
#     file_handle2.writelines('第' + str(i) + '题的答案：' + '\t' + result_end + '\n')
#     file_handle1.close()
# import random
# from fractions import Fraction
#
# file_handle1 = open('Exercises.txt', 'w+')
# file_handle2 = open('Answers.txt', 'w+')
# file_handle1.close()
# file_handle2.close()
# subject_num = 100  # 题目数量
# scope = 10  # 随机数范围
#
# symbol = ['+', '-', '*', '/']
# expressions = set()  # 保存已生成的题目
#
#
# # 自定义比较函数，判断题目是否重复
# def is_duplicate(expression):
#     rpn_expression = convert_to_rpn(expression)
#     return rpn_expression in expressions
#
#
# # 将中缀表达式转换为逆波兰表达式
# def convert_to_rpn(expression):
#     stack = []
#     rpn = []
#     for token in expression:
#         if token in symbol:
#             while stack and stack[-1] in symbol and symbol.index(stack[-1]) >= symbol.index(token):
#                 rpn.append(stack.pop())
#             stack.append(token)
#         else:
#             rpn.append(token)
#     while stack:
#         rpn.append(stack.pop())
#     return tuple(rpn)  # 返回元组以便比较
#
#
# def generate_expression(num_operators):
#     if num_operators == 0:
#         num = random.randint(1, scope)
#         return str(num)
#     else:
#         operator = random.choice(symbol)
#         num1 = generate_expression(num_operators - 1)
#         num2 = generate_expression(num_operators - 1)
#         expression = f"{num1} {operator} {num2}"
#         if random.choice([True, False]):
#             expression = f"({expression})"
#         return expression
#
#
# i = 0
# while i < subject_num:
#     expression = generate_expression(2)  # 生成带括号的表达式，最多两个运算符
#     expression_str = expression
#
#     result = eval(expression_str)  # 题目答案
#     if result < 0 or is_duplicate(expression):
#         continue  # 如果结果小于0或者题目已存在，则重新生成下一个题目
#
#     expressions.add(convert_to_rpn(expression))  # 将题目添加到集合中
#     i += 1
#
#     file_handle1 = open('Exercises.txt', 'a', encoding='utf-8')  # 写入题目
#     file_handle1.writelines('四则运算题目.' + str(i) + '\t' + expression_str + '=' + '\n')
#     file_handle1.close()
#
#     result = Fraction(result).limit_denominator()  # 结果转化为近似分数
#     w = result.numerator
#     r = result.denominator
#     if w > r != 1:  # 判断是否为带分数
#         result_end = str(str(int(w / r)) + "'" + str(w % r) + "/" + str(r))  # 转化为带分数形式
#     else:
#         result_end = str(result)
#
#     file_handle2 = open('Answers.txt', 'a', encoding='utf-8')  # 写入答案
#     file_handle2.writelines('第' + str(i) + '题的答案：' + '\t' + result_end + '\n')
#     file_handle1.close()
import random
from fractions import Fraction
# 命令行参数
import argparse
import re

parser = argparse.ArgumentParser(description='Generate arithmetic expressions.')
parser.add_argument('-n', type=int, help='number of expressions to generate')  # 表达式数量
parser.add_argument('-r', type=int, help='range of values for numbers in expressions')  # 最大数值
parser.add_argument('-e', type=str, help='path to exercises file')  # 测试文件
parser.add_argument('-a', type=str, help='path to answers file')  # 答案文件
args = parser.parse_args()

subject_num = args.n if args.n else 100
scope = args.r if args.r else 10

correct_count = 0
wrong_count = 0

# with open(exercises_file, 'r', encoding='utf-8') as exercises, open(answers_file, 'r', encoding='utf-8') as answers:
#     for line1, line2 in zip(exercises, answers):
#         expression_match = re.match(r'^(.*?)=', line1)
#         result_match = re.search(r'\t(.*)$', line2)
#         if expression_match and result_match:
#             expression = expression_match.group(1).strip()
#             result = result_match.group(1).strip()
#             res=eval(expression)
#             res = Fraction(res).limit_denominator()  # 结果转化为近似分数
#             w = res.numerator
#             r = res.denominator
#             if w > r != 1:  # 判断是否为带分数
#                 result_end = str(str(int(w / r)) + "'" + str(w % r) + "/" + str(r))  # 转化为带分数形式
#             else:
#                 result_end = str(res)
#
#             if  result_end== str(result):
#                 correct_count += 1
#             else:
#                 wrong_count += 1
#
# print(f"Correct answers: {correct_count}")
# print(f"Wrong answers: {wrong_count}")

file_handle1 = open('Exercises.txt', 'w+')
file_handle2 = open('Answers.txt', 'w+')
file_handle1.close()
file_handle2.close()
exercises_file = args.e if args.e else 'test.txt'
answers_file = args.a if args.a else 'ans.txt'
with open(exercises_file, 'r', encoding='utf-8') as exercises, \
        open(answers_file, 'r', encoding='utf-8') as answers, open('Grade.txt', 'w') as grade_file:
    incorrect_questions = []
    correct_questions = []
    for i, (line1, line2) in enumerate(zip(exercises, answers), 1):
        # 正则表达式！！！！！！！
        expression_match = re.match(r'四则运算题目.\d+\t(.*?)=', line1)
        result_match = re.search(r'\t(.*)$', line2)
        if expression_match and result_match:
            expression = expression_match.group(1).strip()
            result = result_match.group(1).strip()
            res = eval(expression)
            res = Fraction(res).limit_denominator()  # 结果转化为近似分数
            w = res.numerator
            r = res.denominator
            if w > r != 1:  # 判断是否为带分数
                result_end = str(str(int(w / r)) + "'" + str(w % r) + "/" + str(r))  # 转化为带分数形式
            else:
                result_end = str(res)

            if result_end == str(result):
                correct_count += 1
                correct_questions.append(str(i))
            else:
                wrong_count += 1
                incorrect_questions.append(str(i))

    grade_file.write(f"Correct: {correct_count} ({', '.join(correct_questions)})\n")
    grade_file.write(f"Wrong: {wrong_count} ({', '.join(incorrect_questions)})\n")
    print(f"Correct answers: {correct_count},({', '.join(correct_questions)})\n")
    print(f"Wrong answers: {wrong_count},({', '.join(incorrect_questions)})\n")
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


def generate_expression(num_operators):
    if num_operators == 0:
        num = random.randint(1, scope)
        return str(num)
    else:
        operator = random.choice(symbol)
        num1 = generate_expression(num_operators - 1)
        num2 = generate_expression(num_operators - 1)

        expression = f"{num1} {operator} {num2}"
        if random.choice([True, False]):
            expression = f"({expression})"
        return expression


i = 0
while i < subject_num:
    expression = generate_expression(2)  # 生成带括号的表达式，最多两个运算符
    expression_str = expression

    try:
        result = eval(expression_str)  # 题目答案
    except ZeroDivisionError:
        continue  # 如果除数为零，则重新生成下一个题目

    if result < 0 or is_duplicate(expression):
        continue  # 如果结果小于0或者题目已存在，则重新生成下一个题目

    expressions.add(convert_to_rpn(expression))  # 将题目添加到集合中
    i += 1

    file_handle1 = open('Exercises.txt', 'a', encoding='utf-8')  # 写入题目
    file_handle1.writelines('四则运算题目.' + str(i) + '\t' + expression_str + '=' + '\n')
    file_handle1.close()

    result = Fraction(result).limit_denominator()  # 结果转化为近似分数
    w = result.numerator
    r = result.denominator
    if r == 0:
        continue
    else:
        if w > r != 1:  # 判断是否为带分数
            result_end = str(str(int(w / r)) + "'" + str(w % r) + "/" + str(r))  # 转化为带分数形式
        else:
            result_end = str(result)

    file_handle2 = open('Answers.txt', 'a', encoding='utf-8')  # 写入答案
    file_handle2.writelines('第' + str(i) + '题的答案：' + '\t' + result_end + '\n')
    file_handle1.close()
