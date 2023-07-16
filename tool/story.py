import json

# 定义 API 密钥
api_key = "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"

# 创建包含密钥的字典
data = {
    "api_key": api_key
}

# 将数据写入 JSON 文件
with open("api_key.json", "w") as json_file:
    json.dump(data, json_file)
