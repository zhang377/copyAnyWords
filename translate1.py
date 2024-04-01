import requests
import random
import json
from hashlib import md5

# 百度翻译API密钥
appid = '20210624000871462'
appkey = '1QLm6fOgr9JFQpdIk5bH'

# 输入文件路径
file_path = r'D:\Files\python_projects\copywords\copyAnyWords\itlesReading\3_4chapter'

# 生成md5哈希值
def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()

# 计算sign参数
def calculate_sign(appid, query, salt, appkey):
    return make_md5(appid + query + str(salt) + appkey)

# 使用百度翻译API进行翻译
def translate_word(word):
    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path
    from_lang = 'en'
    to_lang = 'zh'
    salt = random.randint(32768, 65536)
    sign = calculate_sign(appid, word, salt, appkey)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': word, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}
    response = requests.post(url, data=payload, headers=headers)
    translation = response.json()
    if 'trans_result' in translation:
        dst = translation['trans_result'][0]['dst']
        return dst
    else:
        return ''

# 读取并翻译txt文档中的每个单词
def translate_file(file_path):
    translated_content = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            translation = translate_word(word)
            if translation:
                translated_content.append(f'{word}  {translation}\n')
            else:
                translated_content.append(f'{word}\n')
    return translated_content

# 将翻译结果写回原文档
def write_back_translation(file_path, translated_content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(translated_content)

# 主函数
def main():
    translated_content = translate_file(file_path)
    write_back_translation(file_path, translated_content)
    print("翻译完成并已写回原文档！")

if __name__ == '__main__':
    main()
