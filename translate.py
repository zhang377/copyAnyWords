import requests
import random
import json
from hashlib import md5

# 设置百度翻译API的应用ID和密钥
appid = '20210624000871462'
appkey = '1QLm6fOgr9JFQpdIk5bH'

# 源语言和目标语言
from_lang = 'en'
to_lang = 'zh'

# API请求的地址和路径
endpoint = 'http://api.fanyi.baidu.com'
path = '/api/trans/vip/translate'
url = endpoint + path

# 读取并翻译txt文档中的每个单词，并将词性和释义添加在后面
def translate_file(file_path):
    translated_content = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            salt = random.randint(32768, 65536)
            sign = make_md5(appid + word + str(salt) + appkey)
            payload = {'appid': appid, 'q': word, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}
            response = requests.post(url, data=payload)
            translation = response.json()
            translated_word = translation['trans_result'][0]['dst'] if 'trans_result' in translation else None
            translated_content.append(f'{word}  {translated_word}\n') if translated_word else translated_content.append(f'{word}\n')
    return translated_content

# 计算MD5值
def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()

# 将翻译结果写回原文档
def write_back_translation(file_path, translated_content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(translated_content)

# 主函数
def main():
    file_path = r'D:\Files\python_projects\copywords\copyAnyWords\itlesReading\1and2chapter.txt'
    translated_content = translate_file(file_path)
    write_back_translation(file_path, translated_content)

if __name__ == '__main__':
    main()
