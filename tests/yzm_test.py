import ddddocr

ocr = ddddocr.DdddOcr()

# 注意：使用 'rb' 模式打开图片
with open('original_captcha_3.png', 'rb') as f:
    img_bytes = f.read()

# 进行验证码识别
res = ocr.classification(img_bytes)

print("识别结果：", res)