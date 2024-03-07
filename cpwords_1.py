import pyperclip
import time

# 获取剪贴板内容
clipboard_content = pyperclip.paste()

while True:
    # 读取新的剪贴板内容
    new_clipboard_content = pyperclip.paste()

    # 检查新的剪贴板内容是否与上一次相同，如果不同则写入文件
    if new_clipboard_content != clipboard_content:
        clipboard_content = new_clipboard_content  # 更新剪贴板内容

        # 写入新的内容到文件中
        with open('D:\\Files\\python_projects\\copywords\\copyWords.txt', 'a') as file:
            file.write('\n' + clipboard_content)  # 写入剪贴板内容到下一行的行首

    # 1s后再次检查剪贴板内容
    time.sleep(0.5)
