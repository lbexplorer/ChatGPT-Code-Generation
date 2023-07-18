import json

# 定义 API 密钥
api_key = ""

# 创建包含密钥的字典
data = {
    "api_key": api_key
}

# 将数据写入 JSON 文件
with open("api_key.json", "w") as json_file:
    json.dump(data, json_file)
