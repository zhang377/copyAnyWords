from collections import OrderedDict
import enchant

# 读取原始文件内容
input_file_path = r'D:\Files\python_projects\copywords\copyWords.txt'
output_file_path = r'D:\Files\python_projects\copywords\copyWordsResult.txt'

with open(input_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 去重、转换为小写，并进行拼写检查
unique_words = OrderedDict()
spell_checker = enchant.Dict("en_US")  # 使用英语字典进行拼写检查

for line in lines:
    word = line.strip().lower()
    if word and word not in unique_words and spell_checker.check(word):
        unique_words[word] = True

# 写入处理后的内容到新文件
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write('\n'.join(unique_words.keys()))
