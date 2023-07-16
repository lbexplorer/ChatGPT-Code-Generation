import openai

from tool.get_key import get_key

CANDIDATE_MODEL_TEMPERATURE = 0.7
sydtem_comtent = "一个具有10年Python开发经验的资深软件工程师"  # 服务器端的描述
MODEL_type = "gpt-3.5-turbo"  # 根据实际拥有模型类型


def get_respon(user_content):
    openai.api_key = get_key(r"E:\python\pythonProject1\tool\api_key.json")
    print(openai.api_key)
    respon = openai.ChatCompletion.create(
        model=MODEL_type,
        messages=[
            {"role": "system", "content": sydtem_comtent},
            {"role": "user", "content": user_content}
        ],
        temperature=CANDIDATE_MODEL_TEMPERATURE

    )
    pass


def main():
    test_case = "用python实现：提示手动输入3个不同的3位数区间，输入结束后计算这3个区间的交集，并输出结果区间"
    get_respon(test_case)
    #user_content = input("请输入你的代码需求：")
    pass


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    main()
