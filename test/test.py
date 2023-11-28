import base64

# 读取文本文件中的数据 URL
with open('./test.txt', 'r') as file:
    data_url = file.read()

# 确定数据 URL 的格式（例如："data:image/png;base64"）
format, encoded_data = data_url.split(',', 1)

# 解码 Base64 编码的数据
decoded_data = base64.b64decode(encoded_data)

# 提取文件名（可根据需要进行自定义命名）
filename = "image.png"  # 文件名为 image.png，你可以根据需要修改

# 以二进制模式写入解码后的数据到本地文件
with open(filename, 'wb') as file:
    file.write(decoded_data)

print("图像已保存为", filename)