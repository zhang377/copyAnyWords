import re
import os

# 读取文件中的内容
input_file_path = '/copy.txt'
with open(input_file_path, 'r') as file:
    content = file.readlines()

# 使用正则表达式提取短语
phrases = set()  # 使用集合来存储短语，确保不重复
for line in content:
    line = line.strip()  # 移除行首行尾的空白字符
    if '-' in line:
        phrases.add(line)  # 将包含 "-" 符号的行添加到短语集合中
    elif ' ' in line:
        phrases.add(line)  # 将包含空格的行添加到短语集合中

# 写入提取到的短语到新文件中
output_file_path = 'D:\\Files\\python_projects\\copywords\\phrase.txt'
with open(output_file_path, 'w') as output_file:
    for phrase in phrases:
        output_file.write(phrase + '\n')  # 写入短语到新文件的新行

# 从原始文件中删除已提取的短语
updated_content = [line.strip() for line in content if line.strip() not in phrases]
with open(input_file_path, 'w') as file:
    file.write('\n'.join(updated_content))
