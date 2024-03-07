# 读取文本文件内容到列表
with open('copy.txt', 'r') as file:
    lines = file.readlines()

# 创建一个集合来存储单词，保持顺序
unique_words = []
word_set = set()

# 遍历每行内容，提取单词并去重
for line in lines:
    word = line.strip()  # 去除行尾换行符等空白字符
    if word not in word_set:
        word_set.add(word)
        unique_words.append(word)

# 将去重后的内容写回到文本文件
with open('your_output_file.txt', 'w') as file:
    for word in unique_words:
        file.write(f"{word}\n")
