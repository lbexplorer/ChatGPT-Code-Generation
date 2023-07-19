from Class_chatGPT.Chat_gpt import Chat_gpt


def main():
    user = input("请输入用户名称: ")
    chat = Chat_gpt(user)

    while 1:
        # 限制对话次数
        if len(chat.conversation) >= 11:
            print("******************************")
            print("*********强制重置对话**********")
            print("******************************")
            # 写入之前信息
            chat.writeTojson()
            user = input("请输入用户名称: ")
            chat = Chat_gpt(user)

        question = input(f"【{chat.user}】")
        question = question.strip()
        if question == "0":  # 按下空格，即输入孔字符即可退出
            print("*********退出程序**********")
            chat.writeTojson()  # 保存对话
            break
        if question == "1":  # 表示结束当前对话
            print("**************************")
            print("*********重置对话**********")
            print("**************************")
            # 将信息写入信息
            chat.writeTojson()
            user = input("请输入用户名称: ")
            chat = Chat_gpt(user)  # 生成新的实例
            continue

        # 提问-回答-记录
        chat.conversation.append({"role": "user", "content": question})
        answer = chat.get_chat_respon()
        print(f"【ChatGPT】{answer}")
        chat.conversation.append({"role": "assistant", "content": answer})


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    main()
